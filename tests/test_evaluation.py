import sys
sys.path.append("..")
from src.evaluation import regression_metrics

def test_regression_metrics():
    """Test regression metrics."""
    y_test = [1, 2, 3, 4]
    y_pred = [1, 2, 3, 4]
    metrics = regression_metrics(y_test, y_pred)
    assert metrics["r2"] == 1.0
