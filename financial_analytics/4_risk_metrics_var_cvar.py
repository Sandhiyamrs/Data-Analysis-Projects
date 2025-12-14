import numpy as np

returns = np.random.normal(0.001, 0.02, 1000)

var_95 = np.percentile(returns, 5)
cvar_95 = returns[returns <= var_95].mean()

print("VaR 95%:", var_95)
print("CVaR 95%:", cvar_95)
