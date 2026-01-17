from bayes_opt import BayesianOptimization
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

X, y = load_breast_cancer(return_X_y=True)

def rf_cv(n_estimators, max_depth):
    model = RandomForestClassifier(
        n_estimators=int(n_estimators),
        max_depth=int(max_depth),
        random_state=42
    )
    return cross_val_score(model, X, y, cv=5).mean()

optimizer = BayesianOptimization(
    f=rf_cv,
    pbounds={"n_estimators": (50, 300), "max_depth": (3, 15)},
    random_state=42
)

optimizer.maximize(init_points=5, n_iter=10)
print(optimizer.max)
