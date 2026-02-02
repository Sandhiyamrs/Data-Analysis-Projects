import pandas as pd
import numpy as np

def beta(asset_returns, market_returns):
    cov = np.cov(asset_returns, market_returns)[0][1]
    return cov / np.var(market_returns)

if __name__ == "__main__":
    df = pd.read_csv("datasets/dataset2.csv")
    asset = df["asset"].pct_change().dropna()
    market = df["market"].pct_change().dropna()

    print("Beta:", beta(asset, market))
