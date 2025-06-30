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
