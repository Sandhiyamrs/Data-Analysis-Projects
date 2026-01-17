import requests
import pandas as pd

API_KEY = "YOUR_API_KEY"
SYMBOL = "AAPL"
URL = "https://www.alphavantage.co/query"

def fetch_stock_data():
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": SYMBOL,
        "apikey": API_KEY,
        "outputsize": "compact"
    }

    response = requests.get(URL, params=params)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]

    df = pd.DataFrame(data).T.astype(float)
    df.index = pd.to_datetime(df.index)
    return df.sort_index()

if __name__ == "__main__":
    stock_df = fetch_stock_data()
    print(stock_df.tail())
