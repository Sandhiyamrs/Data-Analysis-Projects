import numpy as np

market = np.array([0.01, 0.02, -0.01, 0.03])
stock = np.array([0.015, 0.025, -0.005, 0.04])

beta = np.cov(stock, market)[0, 1] / np.var(market)
print("Beta:", beta)
