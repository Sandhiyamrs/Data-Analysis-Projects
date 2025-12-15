import numpy as np

values = np.array([10, 12, 11, 13, 100])
threshold = np.mean(values) + 2*np.std(values)

outliers = values[values > threshold]
print("Outliers:", outliers)
