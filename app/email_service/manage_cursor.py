
CURSOR_FILE = "last_history.txt"


def load_cursor(default_id=None):
    try:
        with open(CURSOR_FILE) as f:
            return int(f.read().strip())
    except FileNotFoundError:
        return default_id          # first run uses watch() id

def save_cursor(hid):
    with open(CURSOR_FILE, "w") as f:
        f.write(str(hid))
