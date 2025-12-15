def summary(models):
    return f"Best model accuracy: {max(models.values())}"

print(summary({"RF":0.88,"XGB":0.91}))
