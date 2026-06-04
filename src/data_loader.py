import pandas as pd

def load_raw_data(path="data/raw/Tele-Customer-Churn.csv"):
    """Load raw dataset."""
    return pd.read_csv(path)

def load_processed_data(path="data/processed/cleaned_data.csv"):
    """Load cleaned dataset."""
    return pd.read_csv(path)
