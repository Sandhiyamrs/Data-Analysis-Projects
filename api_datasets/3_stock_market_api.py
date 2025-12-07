"""
Fetch stock data using yfinance and print summary.
Requires: yfinance, pandas
"""
import yfinance as yf
import pandas as pd

def get_stock(symbol='AAPL', period='1mo', interval='1d'):
    ticker = yf.Ticker(symbol)
    df = ticker.history(period=period, interval=interval)
    return df

def summary(df):
    print("Head:\n", df.head())
    print("\nClose stats:\n", df['Close'].describe())

if __name__ == "__main__":
    df = get_stock('AAPL', '3mo')
    summary(df)
