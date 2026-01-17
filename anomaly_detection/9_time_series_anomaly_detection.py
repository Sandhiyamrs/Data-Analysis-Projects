import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

df = pd.read_csv("dataset1.csv", parse_dates=True, index_col=0)

decomposition = seasonal_decompose(
    df.iloc[:, 0],
    model="additive",
    period=12
)

residual = decomposition.resid.dropna()
threshold = residual.std() * 3

anomalies = residual[abs(residual) > threshold]
print(anomalies)
