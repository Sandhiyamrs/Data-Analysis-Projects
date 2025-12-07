"""
Small helper to create charts from CSV and save as PNG
"""
import pandas as pd
import matplotlib.pyplot as plt

def timeseries_line(csv_path, col="value", out="visualizations/timeseries.png"):
    df = pd.read_csv(csv_path)
    df.plot(x='date', y=col)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(out)
    print("Saved", out)
