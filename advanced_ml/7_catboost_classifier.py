from catboost import CatBoostClassifier
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
model = CatBoostClassifier(verbose=0)
model.fit(X, y)

print("Training complete")
