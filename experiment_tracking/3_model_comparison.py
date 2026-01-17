import pandas as pd

def compare_models(results):
    df = pd.DataFrame(results)
    return df.sort_values(by="accuracy", ascending=False)

if __name__ == "__main__":
    model_results = [
        {"model": "RandomForest", "accuracy": 0.88},
        {"model": "XGBoost", "accuracy": 0.90},
        {"model": "SVM", "accuracy": 0.85}
    ]

    comparison = compare_models(model_results)
    print(comparison)
