import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from app.manage_sheet.worksheet import get_worksheet 

def read_rows(SHEET_ID):
    ws = get_worksheet(SHEET_ID)
    rows = ws.get_all_values()

    if not rows:
        return []

    header = rows[0]
    data_rows = rows[1:]

    
    results = [dict(zip(header, row)) for row in data_rows]
    # print(results)
    return results


