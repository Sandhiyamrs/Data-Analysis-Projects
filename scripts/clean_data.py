import pandas as pd

def clean_dataset(path):
    df = pd.read_csv(path)
    df = df.drop_duplicates()
    df = df.fillna(0)
    df.to_csv(path, index=False)
    print("Cleaned:", path)

