import requests
import json
import time
if __name__ == "__main__":
    request = requests.get(
        "https://api.coinbase.com/v2/exchange-rates?currency=ETH"
        )
    if request.status_code == 200:
        print(request.json()['data']['rates']['MXN'])
        datos = request.json()
        
    with open('datos.json', 'w') as file:
        json.dump(datos, file)
