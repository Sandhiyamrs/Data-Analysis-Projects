"""
LSTM time series example using keras (TF).
Requires: tensorflow, numpy, pandas
"""
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

def create_series(n=200):
    t = np.arange(n)
    data = np.sin(0.05*t) + 0.1*np.random.randn(n)
    return pd.DataFrame({"value": data})

def prepare_data(series, lookback=10):
    scaler = MinMaxScaler()
    x = scaler.fit_transform(series)
    X, y = [], []
    for i in range(len(x)-lookback):
        X.append(x[i:i+lookback,0])
        y.append(x[i+lookback,0])
    X = np.array(X).reshape(-1, lookback, 1)
    y = np.array(y)
    return X,y,scaler

def build_model(lookback=10):
    model = Sequential()
    model.add(LSTM(32, input_shape=(lookback,1)))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    return model

if __name__=="__main__":
    df = create_series(300)
    X,y,scaler = prepare_data(df.values, lookback=20)
    model = build_model(20)
    model.fit(X,y, epochs=5, batch_size=16)
    print("Done training")
