import numpy as np
import matplotlib.pyplot as plt
import requests
import time

if __name__ == "__main__":
    plt.ion()
    
    y = []
    X = []
    while True:
        r = requests.get("https://api.coinbase.com/v2/prices/BTC-MXN/buy")
        print(r.json()['data']['amount'])
        
        r2 = requests.get("https://api.coinbase.com/v2/prices/BTC-MXN/sell")
        print(r2.json()['data']['amount'])
        
        if r.status_code == 200 and r2.status_code:
            y.append(r.json()['data']['amount'])
            X.append(r2.json()['data']['amount'])
    
            plt.plot(y)
            plt.xlabel("Valor del bitcoin: azul")
            plt.ylabel("Venta del bitcoin: naranja")
            plt.plot(X)
        
            plt.pause(0.05)
            plt.cla()
            time.sleep(1)