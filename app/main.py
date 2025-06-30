from gemini.main import generate_text
import os
from google import genai
from dotenv import load_dotenv
import schedule
import time
import asyncio
from manage_sheet.write_to_sheet import write_to_sheet
from email_service.setup import get_service,start_pubsub_listener
from gemini.main import generate_text
from email_service.send_message import send_mult_emails
from scrape_data.scrape_news import scrape_ebay_news,scrape_walmart_news
from scrape_data.scrape_product import scrape_ebay_products,scrape_walmart_products
from config import PlayWrightManager,SeleniumManager
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

async def automate_task():
    client = genai.Client(
            api_key=API_KEY
        )
    email_service = get_service()
    seleniumManager = SeleniumManager()
    driver = seleniumManager.get_driver()
    ebay_news=await scrape_ebay_news(driver)
    walmart_news = await scrape_walmart_news(driver)
    seleniumManager.close_driver()
    prompt = f"""
        write professional report based on ecommerce companies competitors news
        from ebay {ebay_news} and news from walmart {walmart_news}
        
    """
    response = generate_text(prompt,client=client)
    
    send_mult_emails(service=email_service,sender="firaol.bulo@a2sv.org",subject="News Summary",message=response)
    time.sleep(10)
    playWrightManager=PlayWrightManager()
    await playWrightManager.setup()
    page = await playWrightManager.get_page()
    ebay_producs=await scrape_ebay_products(page)
    walmart_producs=await scrape_walmart_products(page)
    
    await playWrightManager.close_browser()
    
    write_to_sheet(ebay_producs)
    write_to_sheet(walmart_producs)
    prompt = f"""
        write professional report based on ecommerce companies competitors newly released product
        from ebay {ebay_producs} and  from walmart {walmart_news}
        
    """
    response = generate_text(prompt,client=client)
    
    send_mult_emails(service=email_service,sender="firaol.bulo@a2sv.org",subject="News Summary",message=response)
    
if __name__=="Main":
    asyncio.run(automate_task())
    
    
    
