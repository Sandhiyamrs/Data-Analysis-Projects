"""
Gradient Boosting Regressor (sklearn) example
"""
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

def run_gb():
    data = fetch_california_housing()
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)
    model = GradientBoostingRegressor(n_estimators=200, learning_rate=0.05, max_depth=4)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    print("RMSE:", mean_squared_error(y_test, preds, squared=False))

if __name__ == "__main__":
    run_gb()
