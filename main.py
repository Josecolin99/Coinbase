import requests
import json
import time
if __name__ == "__main__":
    while True:
        r = requests.get("https://api.coinbase.com/v2/exchange-rates?currency=ETH")
        if r.status_code == 200:
            print(r.json()['data']['rates']['MXN'])
        time.sleep(1)
