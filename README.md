<h1 align="center">🕵️‍♂️ Competitive Intelligence Monitoring BOT</h1>

<p align="center">
  <b>Track competitors like a pro — with automation, AI, and elegance.</b><br>
  📰 eCommerce news • 🛒 Product launches • 🤖 AI reports • 📊 Dashboards
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.12+-blue?logo=python">
  <img alt="Streamlit" src="https://img.shields.io/badge/UI-Streamlit-orange?logo=streamlit">
  <img alt="License" src="https://img.shields.io/github/license/your-username/competitive-intelligence-bot">
</p>

---

## 🚀 Overview

A fully automated competitive intelligence tool for **e-commerce analysis**, built to:

- 🔎 Scrape **news** & **product data** from **eBay** and **Walmart**
- 🧠 Summarize updates using **Gemini AI**
- 📩 Email summaries to your team
- 📊 Store results in **Google Sheets**
- 🖥️ Visualize insights with a beautiful **Streamlit dashboard**

---

## 🧰 Tech Stack

| Category        | Tools/Frameworks                                                                 |
|----------------|----------------------------------------------------------------------------------|
| Core Language   | [Python 3.12+](https://www.python.org/)                                          |
| Scraping        | [Selenium](https://www.selenium.dev/) • [Playwright](https://playwright.dev/)    |
| AI Summary      | [Gemini AI](https://deepmind.google/technologies/gemini/)                        |
| Email Delivery  | [Gmail API](https://developers.google.com/gmail/api)                             |
| Data Storage    | [Google Sheets API](https://developers.google.com/sheets/api)                    |
| Dashboard UI    | [Streamlit](https://streamlit.io/)                                               |
| Logging         | [Rich](https://github.com/Textualize/rich)                                       |

---
## 📁 Project Structure
```bash
app/
├── dashboard/
│   └── ui.py                  # 📊 Streamlit dashboard
├── manage_sheet/
│   ├── read_worksheet.py      # 📥 Read from Google Sheets
│   └── write_worksheet.py     # 📤 Write to Google Sheets
├── scraping/
│   ├── ebay_news.py
│   ├── walmart_news.py
│   ├── ebay_products.py
│   └── walmart_products.py
├── gemini/
│   └── gemini_ai.py           # 🤖 Gemini AI API integration
├── email/
│   └── email_service.py       # 📬 Gmail service setup
└── main.py                    # 🧠 Entrypoint script

```
## ⚙️ Setup Instructions
💡 Make sure to use Python 3.12+ and set up Google & Gemini credentials beforehand.

#### 1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/competitive-intelligence-bot.git
cd competitive-intelligence-bot
#### 2. Create a Virtual Environment
```bash
python3 -m venv env
source env/bin/activate
```
#### 3. Install Requirements
```bash
pip install -r requirements.txt
```
#### 4. Add Config Files
Place .env with your keys:
```
GEMINI_API_KEY=your_key_here
GOOGLE_SHEET_ID=your_sheet_id_here

Place token.json and credentials.json from Google Cloud in /config
```
### ▶️ How to Use
🔄 Run Full Automation
```bash
python3 app/main.py
```
📊 Launch Dashboard

```bash
streamlit run app/dashboard/ui.py
```
✨ Example Output (Console)
```
🟢 Script is running...
📰 Collecting News .............
✅ eBay News Collected
✅ Walmart News Collected
🧠 Analyzing with Gemini...
✅ News Summary Saved
📩 Sending Emails...
✅ Messages sent to 4 members
🛒 Scraping Product Listings...
✅ Walmart & eBay products scraped
📈 Updating Google Sheet...
✅ Report Generated & Sent
🎉 Finished.
```
🧠 Sample Email
```
Subject: Products Summary

Gemini AI Report:

📌 Walmart added 3 new products in the electronics category.
📌 eBay introduced 5 limited edition collectibles.
📈 Market trends suggest rising demand for gaming accessories...
```

## 🔐 Advanced Features
✅ Retry logic on failed scraping

✅ Future proxy support for Amazon, BestBuy, etc.

🔄 Modular structure for easy extension

## 🔮 Roadmap
 eBay/Walmart scraping

 Gemini AI integration

 Email dispatch

 Google Sheet sync

 Streamlit dashboard

 Proxy & rotating IP support

 Slack/Telegram bot integration

 CSV export & analytics charts

## 🙋‍♂️ Author
Firaol Bulo
🎓 Software Engineer
🧠 Python Developer
