from sklearn.model_selection import TimeSeriesSplit
import numpy as np

X = np.arange(20)
tscv = TimeSeriesSplit(n_splits=3)

for train, test in tscv.split(X):
    print("Train:", train, "Test:", test)
