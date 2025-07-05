# ========== Login TradingView ==========
from tvDatafeed import TvDatafeed, Interval
import pandas as pd
import requests
import schedule
import time

# Login TradingView
tv = TvDatafeed(
    username='alfathjurdan@gmail.com',
    password='@Lfathjurdan1'
)

# ========== Fungsi Zona Support & Resistance ==========
def cari_zona_sr(data):
    zona = []
    for i in range(2, len(data)):
        if data['low'][i] < data['low'][i-1] and data['low'][i] < data['low'][i-2]:
            zona.append(("support", data['low'][i]))
        elif data['high'][i] > data['high'][i-1] and data['high'][i] > data['high'][i-2]:
            zona.append(("resistance", data['high'][i]))
    return zona[-1] if zona else None

# ========== Fungsi Hitung TP/SL ==========
def hitung_tp_sl(harga, arah, rr):
    pip = 0.10  # 10 pip
    sl = harga - pip if arah == "BUY" else harga + pip
    tp = harga + pip * rr if arah == "BUY" else harga - pip * rr
    return round(sl, 2), round(tp, 2)

# ========== Fungsi Kirim Telegram ==========
TOKEN = "7972077213:AAFzrrlDZL0UkRH6iccMQrFXI_eHRfO149A"
CHAT_ID = 6303041882

def kirim_sinyal(pesan):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": pesan}
    try:
        requests.post(url, data=data)
    except:
        print("❌ Gagal kirim ke Telegram.")

# ========== Daftar Pair ==========
pair_list = ["XAUUSD", "GBPUSD", "USDJPY"]

# ========== Analisa SCALPING ==========
def analisa_scalping():
    for symbol in pair_list:
        data = tv.get_hist(symbol=symbol, exchange='OANDA', interval=Interval.in_1_minute, n_bars=100)
        zona = cari_zona_sr(data)
        if zona:
            arah, harga = ("BUY", zona[1]) if zona[0] == "support" else ("SELL", zona[1])
            sl, tp = hitung_tp_sl(harga, arah, rr=3)
            pesan = f"[AI SCALPING {symbol}]\n{arah} dari zona {zona[0].upper()} di {harga}\nSL: {sl} | TP: {tp}\nRR: 1:3 | TF: M1"
            print(pesan)
            kirim_sinyal(pesan)

# ========== Analisa SWING ==========
def analisa_swing():
    for symbol in pair_list:
        data = tv.get_hist(symbol=symbol, exchange='OANDA', interval=Interval.in_1_hour, n_bars=100)
        zona = cari_zona_sr(data)
        if zona:
            arah, harga = ("BUY", zona[1]) if zona[0] == "support" else ("SELL", zona[1])
            sl, tp = hitung_tp_sl(harga, arah, rr=2)
            pesan = f"[AI SWING {symbol}]\n{arah} dari zona {zona[0].upper()} di {harga}\nSL: {sl} | TP: {tp}\nRR: 1:2 | TF: H1"
            print(pesan)
            kirim_sinyal(pesan)

# ========== Jadwal Otomatis ==========
schedule.every(15).minutes.do(analisa_scalping)
schedule.every().hour.at(":00").do(analisa_swing)

while True:
    schedule.run_pending()
    time.sleep(1)
tvDatafeed
pandas
requests
schedule
pytz
   