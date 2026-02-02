import pandas as pd

def calculate_returns(df, price_col="close"):
    df["returns"] = df[price_col].pct_change()
    return df.dropna()

if __name__ == "__main__":
    df = pd.read_csv("datasets/dataset2.csv")
    df = calculate_returns(df)
    print(df.head())
