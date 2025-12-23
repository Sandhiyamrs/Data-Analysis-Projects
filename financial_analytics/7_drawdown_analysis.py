import numpy as np

prices = np.array([100,105,102,110,108])
cum_max = np.maximum.accumulate(prices)
drawdown = (prices - cum_max) / cum_max

print("Max Drawdown:", drawdown.min())
