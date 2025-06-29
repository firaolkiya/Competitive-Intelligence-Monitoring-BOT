from worksheet import get_worksheet 
def read_rows():
    ws = get_worksheet()
    rows = ws.get_all_values()

    if not rows:
        return []

    header = rows[0]
    data_rows = rows[1:]

    results = [dict(zip(header, row)) for row in data_rows]
    return results