import pandas as pd
import sys
sys.path.append("..")
from src.preprocessing import fix_total_charges

def test_fix_total_charges():
    """Test TotalCharges fix."""
    df = pd.DataFrame({"TotalCharges": ["100", "200", " ", "300"]})
    df = fix_total_charges(df)
    assert df["TotalCharges"].isnull().sum() == 0
