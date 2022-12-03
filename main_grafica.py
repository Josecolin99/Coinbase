import matplotlib.pyplot as plt
import requests
import time

if __name__ == "__main__":
    plt.ion()
    
    y = []
    X = []
    while True:
        request = requests.get("https://api.coinbase.com/v2/prices/BTC-MXN/buy")
        print("Valor: ", request.json()['data']['amount'])
        
        request2 = requests.get("https://api.coinbase.com/v2/prices/BTC-MXN/sell")
        print("Venta: ", request2.json()['data']['amount'])
        
        if request.status_code == 200 and request2.status_code:
            y.append(request.json()['data']['amount'])
            X.append(request2.json()['data']['amount'])
    
            plt.plot(y)
            plt.xlabel("Valor del bitcoin: azul")
            plt.ylabel("Venta del bitcoin: naranja")
            plt.plot(X)
            plt.pause(0.05)
            plt.cla()
            time.sleep(1)