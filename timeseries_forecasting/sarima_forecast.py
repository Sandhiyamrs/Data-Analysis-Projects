"""
SARIMA forecast example using statsmodels
"""
import pandas as pd
import numpy as np
import statsmodels.api as sm

def generate():
    t = np.arange(200)
    y = 10 + 0.5*t + 5*np.sin(0.1*t) + np.random.randn(200)
    return pd.Series(y, index=pd.date_range("2020-01-01", periods=200))

def run_sarima():
    s = generate()
    mod = sm.tsa.SARIMAX(s, order=(1,1,1), seasonal_order=(1,1,1,12))
    res = mod.fit(disp=False)
    print(res.summary())
    pred = res.get_forecast(steps=12)
    print(pred.predicted_mean)

if __name__=="__main__":
    run_sarima()
