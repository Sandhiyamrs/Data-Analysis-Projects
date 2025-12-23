import numpy as np

actual = np.array([100,105,110])
predicted = np.array([98,107,108])

rmse = np.sqrt(np.mean((actual - predicted) ** 2))
print("RMSE:", rmse)
