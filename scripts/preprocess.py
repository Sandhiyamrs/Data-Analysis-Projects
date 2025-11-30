import pandas as pd

def normalize_column(path, column):
    df = pd.read_csv(path)
    df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())
    df.to_csv(path, index=False)
    print(f"Normalized column '{column}' in {path}")

normalize_column("../datasets/dataset1.csv", "sales")

