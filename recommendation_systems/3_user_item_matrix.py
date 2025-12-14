import pandas as pd

data = {
    "User": ["U1", "U1", "U2", "U2", "U3"],
    "Item": ["A", "B", "A", "C", "B"],
    "Rating": [5, 4, 4, 5, 3]
}

df = pd.DataFrame(data)
matrix = df.pivot(index="User", columns="Item", values="Rating").fillna(0)
print(matrix)
