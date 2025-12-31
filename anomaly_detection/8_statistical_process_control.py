import numpy as np

data = np.array([50, 52, 51, 49, 80])
mean = data.mean()
std = data.std()

ucl = mean + 3 * std
lcl = mean - 3 * std

print("UCL:", ucl, "LCL:", lcl)
print("Out of control:", data[(data > ucl) | (data < lcl)])
