# scalping-sinyal-aiimport time
import random
import requests

# Telegram Bot Info
TOKEN = "7972077213:AAFzrrlDZL0UkRH6iccMQrFXI_eHRfO149A"
CHAT_ID ="6303041882"

# Pair yang dianalisis
pair = ['XAUUSD', 'GBPUSD', 'USDJPY']

def kirim_telegram(pesan):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": pesan
    }
    try:
        requests.post(url, data=data)
    except:
        print("Gagal kirim sinyal ke Telegram.")

while True:
    for symbol in pair:
        harga = round(random.uniform(1900, 2000), 2)
        sinyal = random.choice(['BUY 💚', 'SELL ❤️'])
        pesan = f"""📊 [AI Scalping {symbol}]
{sinyal} di harga {harga}
SL: {harga - 5:.2f} | TP: {harga + 10:.2f}
"""
        print(pesan)
        kirim_telegram(pesan)
    time.sleep(15 * 60)  # jeda 15 menit