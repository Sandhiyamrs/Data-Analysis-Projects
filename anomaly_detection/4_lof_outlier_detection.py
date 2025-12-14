from sklearn.neighbors import LocalOutlierFactor
import numpy as np

X = np.array([[10],[12],[11],[13],[100]])
lof = LocalOutlierFactor(n_neighbors=2)
outliers = lof.fit_predict(X)

print("Outlier Labels:", outliers)
