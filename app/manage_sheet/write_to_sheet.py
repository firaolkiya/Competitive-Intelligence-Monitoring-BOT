import os
import dotenv
import gspread
from google.oauth2.service_account import Credentials

dotenv.load_dotenv()

SHEET_ID=os.getenv("PRODUCT_SHEET_ID")

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


def write_to_sheet(data):
    creds = Credentials.from_service_account_file('automation-464318-17d2b37d86f1.json', scopes=SCOPES)

    client = gspread.authorize(creds)

    spreadsheet = client.open_by_key(SHEET_ID if SHEET_ID else "")  # from sheet URL
    worksheet = spreadsheet.worksheet('Sheet1')  # or get_worksheet(0)

    # worksheet.append_row(['Title', 'Price', 'Link', 'Image URL'])

    # Write rows
    for item in data:
        worksheet.append_row([item[0], item[1], item[2], item[3]])
