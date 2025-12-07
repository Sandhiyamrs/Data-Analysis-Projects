"""
Generate advanced plots using seaborn/matplotlib and save as PNGs.
"""
import seaborn as sns, matplotlib.pyplot as plt
import pandas as pd, numpy as np

def run():
    df = pd.DataFrame(np.random.randn(200,4), columns=list("ABCD"))
    sns.pairplot(df)
    plt.savefig("visualizations/pairplot.png", dpi=150)
    print("Saved pairplot to visualizations/pairplot.png")

if __name__=="__main__":
    run()
