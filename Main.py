import time
import random

pair = ['XAUUSD', 'GBPUSD', 'USDJPY']

while True:
    for symbol in pair:
        harga = round(random.uniform(1900, 2000), 2)
        sinyal = random.choice(['BUY 💚', 'SELL ❤️'])
        print(f"[AI Sinyal {symbol}] {sinyal} di harga {harga}")
    time.sleep(15 * 60)
