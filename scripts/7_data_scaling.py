from sklearn.preprocessing import StandardScaler
import numpy as np

X = np.array([[10,20],[30,40]])
scaler = StandardScaler()
print(scaler.fit_transform(X))
