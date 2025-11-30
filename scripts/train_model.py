import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("../datasets/dataset1.csv")

model = LinearRegression()
model.fit(df[['price']], df['sales'])

print("Model trained successfully!")
print("Coefficient:", model.coef_[0])

