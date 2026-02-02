import pandas as pd

def max_drawdown(series):
    cumulative = (1 + series).cumprod()
    peak = cumulative.cummax()
    drawdown = (cumulative - peak) / peak
    return drawdown.min()

if __name__ == "__main__":
    df = pd.read_csv("datasets/dataset2.csv")
    returns = df["close"].pct_change().dropna()

    print("Max Drawdown:", max_drawdown(returns))
