from sklearn.ensemble import StackingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

estimators = [
    ('rf', RandomForestClassifier()),
    ('lr', LogisticRegression(max_iter=200))
]

model = StackingClassifier(
    estimators=estimators,
    final_estimator=LogisticRegression()
)

model.fit(X, y)
print("Stacking model trained")
