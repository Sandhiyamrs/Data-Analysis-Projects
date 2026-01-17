import pandas as pd
from datetime import datetime

DATA_PATH = "datasets/dataset1.csv"
REPORT_PATH = "eda_reports/auto_summary_report.md"

def generate_report():
    df = pd.read_csv(DATA_PATH)

    with open(REPORT_PATH, "w") as f:
        f.write("# Automated Data Summary Report\n\n")
        f.write(f"Generated on: {datetime.now()}\n\n")
        f.write("## Dataset Overview\n")
        f.write(f"- Rows: {df.shape[0]}\n")
        f.write(f"- Columns: {df.shape[1]}\n\n")

        f.write("## Column Summary\n")
        f.write(df.describe().to_markdown())

    print("Report generated successfully.")

if __name__ == "__main__":
    generate_report()
