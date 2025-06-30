from gemini.main import generate_text
import os
from google import genai
from dotenv import load_dotenv
import schedule
import time
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
import asyncio
from manage_sheet.write_to_sheet import write_to_sheet
from email_service.setup import get_service,start_pubsub_listener
from gemini.main import generate_text
from email_service.send_message import send_mult_emails
from scrape_data.scrape_news import scrape_ebay_news,scrape_walmart_news
from scrape_data.scrape_product import scrape_ebay_products,scrape_walmart_products
from config import PlayWrightManager,SeleniumManager
load_dotenv()

NEWS_SUMMARY = "app/data/news_summary.txt"
LOG_FILE = "logs/output.log"

API_KEY = os.getenv("GEMINI_API_KEY")

async def automate_task():
    try:
        console = Console()

        console.rule("[bold green]Competitive Intelligence Monitor")
        console.print("🚀 [bold cyan]Script is running...", style="bold")

        client = genai.Client(api_key=API_KEY)
        email_service = get_service()

        seleniumManager = SeleniumManager()
        driver = seleniumManager.get_driver()

        # ───── NEWS COLLECTION ─────
        console.rule("[yellow]📢 Collecting News")

        with console.status("[bold green]Scraping eBay news..."):
            ebay_news = await scrape_ebay_news(driver)
        console.print("[green]✅ eBay News Collected")

        with console.status("[bold green]Scraping Walmart news..."):
            walmart_news = await scrape_walmart_news(driver)
        console.print("[green]✅ Walmart News Collected")

        seleniumManager.close_driver()

        # ───── NEWS ANALYSIS ─────
        console.rule("[blue]🧠 Analysing News with Gemini")
        prompt = f"""
        Write a professional report based on e-commerce competitors' news.
        eBay News: {ebay_news}
        Walmart News: {walmart_news}
        """

        response = generate_text(prompt, client=client)
        with open(NEWS_SUMMARY, "w+") as f:
            f.write(response if response else "no news")

        console.print("[green]✅ News Analysis Completed")

        # ───── SENDING NEWS EMAILS ─────
        console.rule("[magenta]📬 Sending News Emails")
        send_mult_emails(
            service=email_service,
            sender="firaol.bulo@a2sv.org",
            subject="News Summary",
            message=response
        )
        console.print("[green]✅ News Emails Sent")

        # ───── PRODUCT COLLECTION ─────
        console.rule("[yellow]🛍️ Collecting Product Lists")

        console.print("[cyan]🔧 Setting up Playwright...")
        playWrightManager = PlayWrightManager()
        await playWrightManager.setup()
        page = await playWrightManager.get_page()

        with console.status("[bold green]Scraping Walmart products..."):
            walmart_producs = await scrape_walmart_products(page)
        console.print("[green]✅ Walmart Products Collected")

        with console.status("[bold green]Scraping eBay products..."):
            ebay_producs = await scrape_ebay_products(page)
        console.print("[green]✅ eBay Products Collected")

        await playWrightManager.close_browser()

        # ───── GOOGLE SHEET UPDATE ─────
        console.rule("[blue]📄 Updating Google Sheet")
        write_to_sheet(ebay_producs)
        write_to_sheet(walmart_producs)
        console.print("[green]✅ Google Sheet Updated")

        # ───── PRODUCTS REPORT ─────
        console.rule("[cyan]📈 Creating Products Report with Gemini")
        prompt = f"""
        Write a professional report based on newly released e-commerce products.
        eBay Products: {ebay_producs}
        Walmart Products: {walmart_producs}
        """
        response = generate_text(prompt, client=client)

        console.rule("[magenta]📤 Sending Products Report")
        send_mult_emails(
            service=email_service,
            sender="firaol.bulo@a2sv.org",
            subject="Products Summary",
            message=response
        )
        console.print("[green]✅ Products Emails Sent")

        # ───── COMPLETED ─────
        console.rule("[bold green]✅ All Tasks Completed")
    except Exception as e:
        with open(LOG_FILE,'a') as f:
               f.write(str(e))
if __name__=="__main__":
    service = get_service()
    # send_mult_emails(service=service,sender="firaol.bulo@a2sv.org",subject="Test",message="Test")
    asyncio.run(automate_task())
    
    
    
