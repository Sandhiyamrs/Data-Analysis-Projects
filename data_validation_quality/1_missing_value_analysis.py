import pandas as pd

df = pd.DataFrame({
    "age": [20, None, 25],
    "salary": [30000, 40000, None]
})

print(df.isnull().sum())
