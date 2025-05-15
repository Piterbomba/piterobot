
import time
import requests

BOT_TOKEN = "7731157322:AAFQ7HYzCNfcpzHgUR0wzrSjJBUcc1n9KRg"
CHAT_ID = "@cryptoai_dlanas"

def send_signal(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=data)

def generate_signal():
    return "[Sygnał AI] BTC\nCena: $61,200\nStatus: Odbicie od wsparcia\nMożliwa korekta do $62,000"

while True:
    send_signal(generate_signal())
    time.sleep(6 * 60 * 60)  # 6h
