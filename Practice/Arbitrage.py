import requests
import pandas as pd
import matplotlib.pyplot as asf

link = "https://api.cryptonator.com/api/full/btc-usd"

data=requests.get(link).json()['ticker']['markets']

print(data)

frame=pd.DataFrame(data)

print(frame)
max=max(frame["price"])
min=min(frame["price"])
print(max)
print(min)
arbitrage=float(max)-float(min)
print("Arbitrage: ",arbitrage)
show=asf.scatter(frame["price"],frame["volume"])
#asf.annotate("Cryptonator Data - USD", xy=(frame["price"],frame["volume"]),xytext=(frame["market"]))
for i, txt in enumerate(frame["market"]):
        asf.annotate(txt, (frame["price"][i], frame["volume"][i]))

asf.xticks(rotation=90)
asf.show()