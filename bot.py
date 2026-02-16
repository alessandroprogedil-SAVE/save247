import os
import urllib.parse
import urllib.request
from datetime import datetime

TOKEN = os.environ["TG_BOT_TOKEN"]
CHAT_ID = os.environ["TG_CHAT_ID"]

def send(text: str) -> None:
    msg = urllib.parse.quote(text)
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}"
    with urllib.request.urlopen(url) as r:
        r.read()

if __name__ == "__main__":
    now = datetime.now().strftime("%d/%m %H:%M")
    send(f"SAVE’ 24/7 online ✅ ({now})")
