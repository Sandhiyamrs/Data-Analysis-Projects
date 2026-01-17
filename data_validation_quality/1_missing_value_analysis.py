import pandas as pd

def missing_value_report(df):
    report = pd.DataFrame({
        "missing_count": df.isnull().sum(),
        "missing_percentage": df.isnull().mean() * 100
    })
    return report[report["missing_count"] > 0]

if __name__ == "__main__":
    df = pd.read_csv("datasets/dataset1.csv")
    report = missing_value_report(df)
    print(report)
