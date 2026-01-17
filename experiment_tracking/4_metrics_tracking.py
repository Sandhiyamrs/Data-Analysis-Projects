import pandas as pd
from datetime import datetime

METRICS_FILE = "experiment_tracking/metrics_history.csv"

def track_metrics(model_name, metrics):
    row = {
        "timestamp": datetime.now(),
        "model": model_name,
        **metrics
    }

    df = pd.DataFrame([row])

    try:
        df_existing = pd.read_csv(METRICS_FILE)
        df = pd.concat([df_existing, df], ignore_index=True)
    except FileNotFoundError:
        pass

    df.to_csv(METRICS_FILE, index=False)
    print("Metrics tracked successfully.")

if __name__ == "__main__":
    track_metrics(
        "LogisticRegression",
        {"accuracy": 0.84, "precision": 0.82, "recall": 0.80}
    )

