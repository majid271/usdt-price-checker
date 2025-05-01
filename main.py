import requests
import time
from datetime import datetime

THRESHOLD = 400  # اختلاف قیمت برای هشدار

def get_nobitex_usdt_price():
    try:
        url = "https://api.nobitex.ir/market/stats"
        payload = {"srcCurrency": "usdt", "dstCurrency": "rls"}
        response = requests.post(url, data=payload)
        data = response.json()
        return int(float(data['stats']['usdt-rls']['latest']))
    except:
        return None

def get_wallex_usdt_price():
    try:
        url = "https://api.wallex.ir/v1/markets/usdt-rls"
        response = requests.get(url)
        data = response.json()
        return int(float(data['result']['price']))
    except:
        return None

def run_checker():
    print("📡 ربات بررسی اختلاف قیمت تتر بین نوبیتکس و والکس")
    while True:
        nobitex_price = get_nobitex_usdt_price()
        wallex_price = get_wallex_usdt_price()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if nobitex_price and wallex_price:
            diff = abs(nobitex_price - wallex_price)
            print(f"\n🕒 {now}")
            print(f"💰 نوبیتکس: {nobitex_price:,} تومان")
            print(f"💰 والکس:   {wallex_price:,} تومان")
            print(f"🔁 اختلاف قیمت: {diff:,} تومان")

            if diff >= THRESHOLD:
                print("🚨 هشدار: اختلاف قیمت از حد مجاز بیشتر است!")

        else:
            print(f"\n🕒 {now} | ⚠️ خطا در دریافت داده‌ها")

        time.sleep(60)

if __name__ == "__main__":
    run_checker()
