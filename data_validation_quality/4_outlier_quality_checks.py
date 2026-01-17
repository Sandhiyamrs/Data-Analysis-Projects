import pandas as pd

def detect_outliers_iqr(series):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return series[(series < lower) | (series > upper)]

if __name__ == "__main__":
    df = pd.read_csv("datasets/dataset1.csv")

    for col in df.select_dtypes(include=["int64", "float64"]).columns:
        outliers = detect_outliers_iqr(df[col])
        print(f"{col}: {len(outliers)} outliers detected")
