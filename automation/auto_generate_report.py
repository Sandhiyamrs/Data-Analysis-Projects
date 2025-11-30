import pandas as pd

df = pd.read_csv('../datasets/dataset1.csv')

report = f"""
Sales Auto Report
-----------------
Max sales: {df['sales'].max()}
Min sales: {df['sales'].min()}
Average: {df['sales'].mean()}
"""

open("sales_report.txt","w").write(report)

print("Report generated!")
