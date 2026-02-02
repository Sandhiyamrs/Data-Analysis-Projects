import numpy as np
import pandas as pd

def sharpe_ratio(returns, risk_free_rate=0.01):
    excess = returns - risk_free_rate / 252
    return np.sqrt(252) * excess.mean() / excess.std()

if __name__ == "__main__":
    df = pd.read_csv("datasets/dataset2.csv")
    returns = df["close"].pct_change().dropna()

    print("Sharpe Ratio:", sharpe_ratio(returns))
