models = {
    "RF": 0.88,
    "XGBoost": 0.91,
    "SVM": 0.86
}

best = max(models, key=models.get)
print("Best Model:", best)
