import numpy as np

data = np.array([10, 12, 13, 12, 11, 99])

q1, q3 = np.percentile(data, [25, 75])
iqr = q3 - q1

outliers = data[(data < q1 - 1.5*iqr) | (data > q3 + 1.5*iqr)]
print("Outliers:", outliers)
