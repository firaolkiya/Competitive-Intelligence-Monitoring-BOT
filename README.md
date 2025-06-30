📊 Competitive Intelligence Monitoring BOT
An automated competitive intelligence tool that monitors major e-commerce platforms like eBay and Walmart for:

✅ Latest News
✅ New Product Listings
✅ Product Trends

Then generates professional reports using Gemini AI, stores data in Google Sheets, and sends insightful summaries via email — all in one pipeline!

🌟 Features
🔍 Scrape e-commerce news and products using:

Selenium (for news)

Playwright (for products)

🤖 Generate detailed summaries using Gemini AI

📩 Send reports via email to team members

📈 Auto-update Google Sheets for data archiving

🌐 Supports proxy and retry logic for stability and large-scale scraping

🖥️ Beautiful Streamlit dashboard for real-time visualization

🚀 How It Works
mermaid
Copy
Edit
graph TD
    A[Run Script] --> B[Scrape eBay & Walmart News]
    B --> C[Analyze with Gemini AI]
    C --> D[Send News Report via Email]
    D --> E[Scrape Product Listings]
    E --> F[Update Google Sheet]
    F --> G[Generate Product Report]
    G --> H[Send Product Report via Email]
🗂️ Project Structure
bash
Copy
Edit
app/
├── dashboard/
│   └── ui.py               # Streamlit dashboard
├── manage_sheet/
│   ├── read_worksheet.py   # Read from Google Sheets
│   └── write_worksheet.py  # Write to Google Sheets
├── scraping/
│   ├── ebay_news.py
│   ├── walmart_news.py
│   ├── ebay_products.py
│   └── walmart_products.py
├── gemini/
│   └── gemini_ai.py        # AI summarization
├── email/
│   └── email_service.py    # Gmail API integration
└── main.py                 # Entrypoint
🧠 Tech Stack
Tool	Purpose
Python 3.12+	Core language
Selenium	News scraping
Playwright (async)	Product scraping
Gemini AI	Report generation
Gmail API	Email delivery
gspread / Google API	Sheets integration
Streamlit	UI dashboard
Rich	Beautiful terminal logs

⚙️ Setup Instructions
Clone the repo

bash
Copy
Edit
git clone https://github.com/your-username/competitive-intelligence-bot.git
cd competitive-intelligence-bot
Set up virtual environment

bash
Copy
Edit
python3 -m venv env
source env/bin/activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set up credentials

.env file for:

GOOGLE_SHEET_ID

GEMINI_API_KEY

Gmail credentials (token.json / credentials.json)

Place your Google credentials in /credentials/ or /config/

▶️ Run the Script
bash
Copy
Edit
python3 app/main.py
📊 Launch Dashboard
bash
Copy
Edit
streamlit run app/dashboard/ui.py
📬 Example Email Output
✉️ Subject: News Summary
“Based on the latest eBay updates, the following strategic shifts are underway...”

✉️ Subject: Products Summary
“Walmart released 5 new product lines this week. Notably...”

🔐 Proxy & Retry Logic
✅ Built-in retry mechanism and future-proofed for proxy support, enabling robust scraping of sites like Amazon, BestBuy, etc.

📅 Roadmap
 eBay & Walmart scraping

 Gemini-based summarization

 Email integration

 Google Sheets update

 Streamlit UI

 Proxy & rotating IP support

 Amazon/BestBuy support

 Slack/Telegram bot notifications

🧑‍💻 Maintained by
Firaol Bulo

Software Engineer

