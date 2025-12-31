from skopt import BayesSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

search = BayesSearchCV(
    RandomForestClassifier(),
    {
        'n_estimators': (50, 300),
        'max_depth': (3, 20)
    },
    n_iter=10
)

search.fit(X, y)
print("Best Params:", search.best_params_)
