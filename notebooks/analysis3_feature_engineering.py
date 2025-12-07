"""
Feature engineering examples:
- create rolling features
- create time-based features
"""
import pandas as pd
import numpy as np

def example():
    date = pd.date_range("2024-01-01", periods=30, freq='D')
    df = pd.DataFrame({"date": date, "value": np.random.randn(30).cumsum()})
    df['day'] = df['date'].dt.day
    df['weekday'] = df['date'].dt.weekday
    df['value_lag1'] = df['value'].shift(1)
    df['rolling_mean_3'] = df['value'].rolling(3).mean()
    print(df.head(10))
    return df

if __name__ == "__main__":
    example()
