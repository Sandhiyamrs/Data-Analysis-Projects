import numpy as np

series = np.array([100, 102, 101, 500, 103])
threshold = series.mean() + 2 * series.std()

anomalies = series[series > threshold]
print("Time series anomalies:", anomalies)
