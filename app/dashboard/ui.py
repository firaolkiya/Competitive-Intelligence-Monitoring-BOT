import streamlit as st
import pandas as pd
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from  app.manage_sheet.read_worksheet import read_rows
import dotenv
import subprocess

dotenv.load_dotenv()
SHEET_ID=os.getenv("PRODUCT_SHEET_ID")
# --- Constants ---
NEWS_SUMMARY = "app/data/news_summary.txt"
LOG_FILE = "logs/output.log"

# --- Setup Streamlit UI ---
st.set_page_config(page_title="Competitive Intelligence Dashboard", layout="wide")
st.title("📊 Competitive Intelligence Monitoring Dashboard")
st.markdown("Monitor real-time competitor updates, product listings, and email reports.")

# --- Sidebar Navigation ---
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to",  ["Overview", "Product Listings", "News & Summaries", "Logs"])

# --- Google Sheets Product Loader ---
@st.cache_data
def load_products_from_sheet():
    rows = read_rows(SHEET_ID)
    return pd.DataFrame(rows)

# --- Overview Page ---
if page == "Overview":
    st.subheader("🧠 System Summary")

    # Run Scraper Button
    
    col1, col2, col3 = st.columns(3)
    col1.metric("🛍️ Products Scraped", "25")
    col2.metric("📰 News Articles", "8")
    col3.metric("📧 Last Email Sent", "10 mins ago")

    st.markdown("### ✅ Latest Run Status")
    st.success("All tasks completed successfully.")
    st.info("Next scheduled run in 12 hours")

# --- Product Listings Page ---
elif page == "Product Listings":
    st.subheader("🛒 Product Listings")
    if st.button("🔁 Re run script"):
        try:
            with st.spinner("Running..."):
                subprocess.run(["python3", "app/main.py"])
        except subprocess.CalledProcessError as e:
            print(f"Script failed with return code {e.returncode}")
        st.success("✅ Scraper run completed!")
    try:
        df = load_products_from_sheet()

        if df.empty:
            st.warning("Google Sheet is empty or not loaded properly.")
        else:
            # Filter by company if available
            if "company" in df.columns:
                companies = ["All"] + sorted(df["company"].unique())
                selected = st.selectbox("Filter by company", companies)
                if selected != "All":
                    df = df[df["company"] == selected]

            # Display products in a styled table
            def highlight_max(s):
                is_max = s == s.max()
                return ['background-color: #28a745' if v else '' for v in is_max]

            # Example: Highlight max price if price column exists
            if "price" in df.columns:
                styled_df = df.style.apply(highlight_max, subset=["price"])
                st.dataframe(styled_df, use_container_width=True)
            else:
                st.dataframe(df.head(20), use_container_width=True)

    except Exception as e:
        st.error(f"Failed to load data from Google Sheets: {e}")

# --- News Summaries Page ---
elif page == "News & Summaries":
    st.subheader("🗞️ News Summary")

    if os.path.exists(NEWS_SUMMARY):
        with open(NEWS_SUMMARY, "r") as f:
            summary = f.read()

        # Display news as styled markdown post (better than textarea)
        st.markdown(
    f"""
    <div style="
        background-color:#f9f9f9; 
        color: #333333;             /* dark text color */
        padding: 20px; 
        border-radius: 10px; 
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        font-family: 'Georgia', serif;
        line-height: 1.6;
        white-space: pre-wrap;
    ">
        {summary}
    </div>
    """,
    unsafe_allow_html=True,
)

    else:
        st.warning("No news summary found yet.")

# --- Logs Page ---
elif page == "Logs":
    st.subheader("📜 Logs")

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = f.readlines()[-30:]  # Show last 30 lines
            st.text("".join(logs))
    else:
        st.warning("Log file not found.")