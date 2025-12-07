"""
Run a simple ML pipeline automatically:
1. clean -> preprocess -> train -> evaluate
This script assumes functions exist in scripts/*.py
"""
import importlib
import sys

def run_pipeline():
    # dynamic import of your scripts
    try:
        clean = importlib.import_module("scripts.clean_data")
        preprocess = importlib.import_module("scripts.preprocess")
        train = importlib.import_module("scripts.train_model")
    except Exception as e:
        print("Make sure scripts.clean_data, scripts.preprocess, scripts.train_model exist:", e)
        sys.exit(1)

    print("Starting pipeline...")
    clean.clean_raw()           # expected function
    preprocess.preprocess()     # expected function
    train.train_and_save_model()# expected function
    print("Pipeline finished.")

if __name__ == "__main__":
    run_pipeline()
