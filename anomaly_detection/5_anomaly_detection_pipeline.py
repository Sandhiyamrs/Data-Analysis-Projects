import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest

class AnomalyPipeline:
    def __init__(self):
        self.scaler = StandardScaler()
        self.model = IsolationForest(
            contamination=0.05,
            random_state=42
        )

    def fit(self, X):
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled)

    def predict(self, X):
        X_scaled = self.scaler.transform(X)
        return self.model.predict(X_scaled)

if __name__ == "__main__":
    df = pd.read_csv("dataset1.csv")
    pipeline = AnomalyPipeline()
    pipeline.fit(df)
    df["anomaly"] = pipeline.predict(df)
    print(df[df["anomaly"] == -1])
