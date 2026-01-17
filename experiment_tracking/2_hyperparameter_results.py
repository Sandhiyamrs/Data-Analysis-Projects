import pandas as pd

def save_hyperparameter_results(results, output_path):
    df = pd.DataFrame(results)
    df.to_csv(output_path, index=False)
    print("Hyperparameter results saved.")

if __name__ == "__main__":
    results = [
        {"max_depth": 3, "accuracy": 0.81},
        {"max_depth": 5, "accuracy": 0.85},
        {"max_depth": 7, "accuracy": 0.88}
    ]

    save_hyperparameter_results(
        results,
        "experiment_tracking/hyperparameter_results.csv"
    )
