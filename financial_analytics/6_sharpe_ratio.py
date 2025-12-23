import numpy as np

returns = np.array([0.02, 0.01, -0.01, 0.03])
risk_free_rate = 0.005

sharpe = (returns.mean() - risk_free_rate) / returns.std()
print("Sharpe Ratio:", sharpe)
