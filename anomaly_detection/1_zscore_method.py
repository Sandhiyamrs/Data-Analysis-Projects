import numpy as np
import pandas as pd

def detect_anomalies_zscore(data, threshold=3):
    mean = np.mean(data)
    std = np.std(data)
    z_scores = [(x - mean) / std for x in data]
    return np.where(np.abs(z_scores) > threshold)

if __name__ == "__main__":
    df = pd.read_csv("dataset1.csv")
    anomalies = detect_anomalies_zscore(df.iloc[:, 0])
    print("Anomaly indices:", anomalies)
