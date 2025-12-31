from statsmodels.tsa.seasonal import seasonal_decompose

data = [10,12,15,10,12,15,10,12,15]
result = seasonal_decompose(data, model='additive', period=3)

print("Seasonal component extracted")
