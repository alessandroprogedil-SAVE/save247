import os
import urllib.parse
import urllib.request
from datetime import datetime

TOKEN = os.environ["TG_BOT_TOKEN"]
CHAT_ID = os.environ["TG_CHAT_ID"]

def send(text: str) -> None:
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = urllib.parse.urlencode({
        "chat_id": CHAT_ID,
        "text": text.strip()
    }).encode()

    req = urllib.request.Request(url, data=data)

    with urllib.request.urlopen(req) as r:
        r.read()

if __name__ == "__main__":
    now = datetime.now().strftime("%d/%m %H:%M")
    send(f"SAVE’ 24/7 online ✅ ({now})")
