import pandas as pd

def detect_iqr_outliers(series):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return series[(series < lower) | (series > upper)]

if __name__ == "__main__":
    df = pd.read_csv("dataset1.csv")
    outliers = detect_iqr_outliers(df.iloc[:, 0])
    print(outliers)
