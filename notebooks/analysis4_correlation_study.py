"""
Correlation study between variables with heatmap data output (CSV).
"""
import pandas as pd
import numpy as np

def create_example():
    df = pd.DataFrame(np.random.randn(100,5), columns=list("ABCDE"))
    corr = df.corr()
    corr.to_csv("visualizations/corr_matrix.csv")
    print("Saved correlation matrix to visualizations/corr_matrix.csv")
    return corr

if __name__ == "__main__":
    print(create_example())
