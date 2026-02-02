import numpy as np
import pandas as pd

def var_cvar(returns, confidence=0.95):
    var = np.percentile(returns, (1 - confidence) * 100)
    cvar = returns[returns <= var].mean()
    return var, cvar

if __name__ == "__main__":
    df = pd.read_csv("datasets/dataset2.csv")
    returns = df["close"].pct_change().dropna()

    var, cvar = var_cvar(returns)
    print("VaR:", var)
    print("CVaR:", cvar)
