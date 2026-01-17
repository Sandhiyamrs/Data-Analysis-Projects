import json
from datetime import datetime

LOG_FILE = "experiment_tracking/experiments_log.json"

def log_experiment(params, metrics, model_name):
    experiment = {
        "timestamp": datetime.now().isoformat(),
        "model": model_name,
        "parameters": params,
        "metrics": metrics
    }

    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except FileNotFoundError:
        logs = []

    logs.append(experiment)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)

    print("Experiment logged successfully.")

if __name__ == "__main__":
    log_experiment(
        params={"n_estimators": 100, "max_depth": 5},
        metrics={"accuracy": 0.87},
        model_name="RandomForest"
    )
