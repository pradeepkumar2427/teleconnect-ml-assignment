import pandas as pd
import sys
sys.path.append("..")
from src.preprocessing import fix_total_charges, encode_features

def test_fix_total_charges():
    """Test TotalCharges fix."""
    df = pd.DataFrame({"TotalCharges": ["100", "200", " ", "300"]})
    df = fix_total_charges(df)
    assert df["TotalCharges"].isnull().sum() == 0

def test_fix_total_charges_type():
    """Test TotalCharges is numeric after fix."""
    df = pd.DataFrame({"TotalCharges": ["100", "200", " "]})
    df = fix_total_charges(df)
    assert df["TotalCharges"].dtype in ["float64", "int64"]

def test_encode_features():
    """Test feature encoding removes object columns."""
    df = pd.DataFrame({"gender": ["Male", "Female"], "tenure": [1, 2]})
    df_encoded = encode_features(df)
    assert "gender" not in df_encoded.columns

def test_encode_features_shape():
    """Test encoding increases columns."""
    df = pd.DataFrame({"gender": ["Male", "Female"], "tenure": [1, 2]})
    df_encoded = encode_features(df)
    assert df_encoded.shape[1] >= df.shape[1]
