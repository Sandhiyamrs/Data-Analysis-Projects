"""
SVM classifier example with standard scaling and grid search option.
Requires: scikit-learn, pandas
"""
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score

def run_svm():
    data = load_wine(as_frame=True)
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    pipe = Pipeline([('scaler', StandardScaler()), ('svc', SVC())])
    params = {'svc__C':[0.1,1,10], 'svc__kernel':['rbf','linear']}
    grid = GridSearchCV(pipe, params, cv=5, n_jobs=-1)
    grid.fit(X_train, y_train)
    print("Best params:", grid.best_params_)
    preds = grid.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, preds))
    print(classification_report(y_test, preds))

if __name__ == "__main__":
    run_svm()
