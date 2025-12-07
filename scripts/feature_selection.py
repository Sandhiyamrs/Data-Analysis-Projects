"""
Feature selection utilities: variance threshold + mutual info
"""
import pandas as pd
from sklearn.feature_selection import VarianceThreshold, mutual_info_classif

def variance_thresh(X, thresh=0.0):
    sel = VarianceThreshold(threshold=thresh)
    X_sel = sel.fit_transform(X)
    return X_sel, sel.get_support(indices=True)

def mutual_info(X, y, k=10):
    mi = mutual_info_classif(X, y)
    idx = mi.argsort()[::-1][:k]
    return idx, mi[idx]

if __name__=="__main__":
    from sklearn.datasets import load_breast_cancer
    data = load_breast_cancer(as_frame=True)
    X = data.data; y = data.target
    print("Top features by MI:", mutual_info(X,y,5))
