import numpy as np

returns = np.array([0.12, 0.10, 0.07])
weights = np.array([0.4, 0.4, 0.2])

portfolio_return = np.dot(weights, returns)
print("Portfolio Return:", portfolio_return)
