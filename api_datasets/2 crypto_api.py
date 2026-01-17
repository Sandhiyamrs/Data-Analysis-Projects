import requests

URL = "https://api.coingecko.com/api/v3/simple/price"
PARAMS = {
    "ids": "bitcoin,ethereum",
    "vs_currencies": "usd"
}

def fetch_crypto_prices():
    response = requests.get(URL, params=PARAMS)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    prices = fetch_crypto_prices()
    for coin, price in prices.items():
        print(f"{coin.upper()} price: ${price['usd']}")
