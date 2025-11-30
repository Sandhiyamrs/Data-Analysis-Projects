import requests
import pandas as pd

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

price = requests.get(url).json()

df = pd.DataFrame([{
    "BTC_USD": price["bpi"]["USD"]["rate_float"]
}])

df.to_csv("crypto_price.csv", index=False)
