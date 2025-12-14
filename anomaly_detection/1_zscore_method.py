import numpy as np
from scipy.stats import zscore

data = np.array([10, 12, 13, 12, 11, 99])
z = zscore(data)

print("Anomalies:", data[abs(z) > 2])
