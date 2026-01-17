import pandas as pd
from datetime import datetime

OUTPUT_PATH = "eda_reports/data_quality_report.md"

def generate_quality_report(df):
    with open(OUTPUT_PATH, "w") as f:
        f.write("# Data Quality Report\n\n")
        f.write(f"Generated on: {datetime.now()}\n\n")

        f.write("## Missing Values\n")
        f.write(df.isnull().sum().to_markdown())
        f.write("\n\n")

        f.write("## Data Types\n")
        f.write(df.dtypes.to_frame("dtype").to_markdown())
        f.write("\n\n")

        f.write("## Statistical Summary\n")
        f.write(df.describe().to_markdown())

if __name__ == "__main__":
    df = pd.read_csv("datasets/dataset1.csv")
    generate_quality_report(df)
    print("Data quality report generated.")
