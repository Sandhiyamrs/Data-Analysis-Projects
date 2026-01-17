import pandas as pd

def generate_summary(metrics_file):
    df = pd.read_csv(metrics_file)

    summary = df.groupby("model").agg(
        avg_accuracy=("accuracy", "mean"),
        runs=("model", "count")
    )

    print("Experiment Summary:")
    print(summary)

if __name__ == "__main__":
    generate_summary("experiment_tracking/metrics_history.csv")
