"""
Hyperparameter tuning example using RandomizedSearchCV
"""
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
import numpy as np

def tune():
    X,y = load_iris(return_X_y=True)
    rf = RandomForestClassifier()
    params = {'n_estimators':[50,100,200], 'max_depth':[None,5,10], 'min_samples_split':[2,5]}
    search = RandomizedSearchCV(rf, params, n_iter=6, cv=3, n_jobs=-1)
    search.fit(X,y)
    print("Best:", search.best_params_)
if __name__=="__main__":
    tune()
