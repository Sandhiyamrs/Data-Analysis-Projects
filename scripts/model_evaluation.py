"""
Model evaluation helpers: classification and regression metrics, save report.
"""
import json
from sklearn.metrics import classification_report, accuracy_score, mean_squared_error

def save_classification_report(y_true, y_pred, path="reports/classification_report.json"):
    report = classification_report(y_true, y_pred, output_dict=True)
    with open(path, "w") as f:
        json.dump(report, f, indent=2)
    print("Saved classification report to", path)

def regression_metrics(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    rmse = mse**0.5
    return {"mse":mse, "rmse":rmse}
