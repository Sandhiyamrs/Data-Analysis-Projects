import pandas as pd

def check_negative_values(df, columns):
    inconsistencies = {}
    for col in columns:
        invalid = df[df[col] < 0]
        if not invalid.empty:
            inconsistencies[col] = invalid
    return inconsistencies

if __name__ == "__main__":
    df = pd.read_csv("datasets/dataset1.csv")

    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    issues = check_negative_values(df, numeric_cols)

    if issues:
        for col, rows in issues.items():
            print(f"Inconsistencies in column: {col}")
            print(rows)
    else:
        print("No consistency issues found.")
