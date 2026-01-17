import pandas as pd
import numpy as np

df = pd.read_csv("dataset1.csv")
values = df.iloc[:, 0]

mean = values.mean()
std = values.std()

ucl = mean + 3 * std
lcl = mean - 3 * std

df["out_of_control"] = (values > ucl) | (values < lcl)

print(df[df["out_of_control"]])
