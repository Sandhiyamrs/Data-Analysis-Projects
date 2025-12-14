import pandas as pd

prices = pd.Series([100, 102, 101, 105, 110])
returns = prices.pct_change()

print("Daily Returns:")
print(returns)
