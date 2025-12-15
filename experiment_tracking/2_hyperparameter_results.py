results = [
    {"lr": 0.01, "accuracy": 0.88},
    {"lr": 0.05, "accuracy": 0.91},
    {"lr": 0.1, "accuracy": 0.89}
]

best = max(results, key=lambda x: x["accuracy"])
print(best)
