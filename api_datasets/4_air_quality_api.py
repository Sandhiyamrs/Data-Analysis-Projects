"""
Simple Air Quality fetcher using OpenAQ API (public).
Requires: requests, pandas
"""
import requests
import pandas as pd

API_BASE = "https://api.openaq.org/v2/latest"

def get_latest_city(city="Delhi", country=None, limit=100):
    params = {"city": city, "limit": limit}
    if country:
        params['country'] = country
    res = requests.get(API_BASE, params=params)
    res.raise_for_status()
    data = res.json()
    results = data.get('results', [])
    # convert to DataFrame
    rows = []
    for r in results:
        loc = r.get('location')
        for m in r.get('measurements', []):
            rows.append({
                'location': loc,
                'parameter': m['parameter'],
                'value': m['value'],
                'unit': m['unit'],
                'lastUpdated': m['lastUpdated']
            })
    return pd.DataFrame(rows)

if __name__ == "__main__":
    df = get_latest_city("Delhi")
    print(df.head())
