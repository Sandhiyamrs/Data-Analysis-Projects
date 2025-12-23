from statsmodels.tsa.holtwinters import ExponentialSmoothing

data = [10,12,13,15,18,20]
model = ExponentialSmoothing(data).fit()
forecast = model.forecast(3)

print("Forecast:", forecast)
