from imblearn.over_sampling import SMOTE
import numpy as np

X = np.array([[1],[2],[3],[4]])
y = np.array([0,0,0,1])

X_res, y_res = SMOTE().fit_resample(X, y)
print(y_res)
