import pandas as pd
from sklearn.preprocessing import StandardScaler

def fix_total_charges(df):
    """Fix TotalCharges column."""
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df["TotalCharges"].fillna(df["TotalCharges"].median(), inplace=True)
    return df

def encode_features(df):
    """Encode categorical features."""
    categorical_cols = df.select_dtypes(include=["object"]).columns
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    return df

def scale_features(X_train, X_test, cols):
    """Scale numerical features."""
    scaler = StandardScaler()
    X_train[cols] = scaler.fit_transform(X_train[cols])
    X_test[cols] = scaler.transform(X_test[cols])
    return X_train, X_test, scaler
