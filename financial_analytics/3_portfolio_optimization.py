import numpy as np
import pandas as pd

def portfolio_performance(weights, returns):
    return np.dot(returns.mean(), weights)

if __name__ == "__main__":
    df = pd.read_csv("datasets/dataset2.csv")
    returns = df.pct_change().dropna()

    weights = np.array([1 / returns.shape[1]] * returns.shape[1])
    expected_return = portfolio_performance(weights, returns)

    print("Expected Portfolio Return:", expected_return)
