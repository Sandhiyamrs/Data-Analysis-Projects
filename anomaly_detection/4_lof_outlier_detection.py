import pandas as pd
from sklearn.neighbors import LocalOutlierFactor

df = pd.read_csv("dataset1.csv")

lof = LocalOutlierFactor(
    n_neighbors=20,
    contamination=0.05
)

df["anomaly"] = lof.fit_predict(df)
outliers = df[df["anomaly"] == -1]

print(outliers)
