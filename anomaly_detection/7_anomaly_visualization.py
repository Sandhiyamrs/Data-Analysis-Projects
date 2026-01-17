import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

df = pd.read_csv("dataset1.csv")

model = IsolationForest(contamination=0.05, random_state=42)
df["anomaly"] = model.fit_predict(df)

plt.figure(figsize=(10, 5))
plt.plot(df.index, df.iloc[:, 0], label="Data")
plt.scatter(
    df[df["anomaly"] == -1].index,
    df[df["anomaly"] == -1].iloc[:, 0],
    color="red",
    label="Anomalies"
)
plt.legend()
plt.show()
