import sys
sys.path.append("..")
from src.evaluation import regression_metrics, classification_metrics

def test_regression_metrics_perfect():
    """Test regression metrics with perfect predictions."""
    y_test = [1, 2, 3, 4]
    y_pred = [1, 2, 3, 4]
    metrics = regression_metrics(y_test, y_pred)
    assert metrics["r2"] == 1.0

def test_regression_metrics_mae():
    """Test MAE calculation."""
    y_test = [1, 2, 3, 4]
    y_pred = [2, 3, 4, 5]
    metrics = regression_metrics(y_test, y_pred)
    assert metrics["mae"] == 1.0

def test_regression_metrics_keys():
    """Test all metric keys present."""
    y_test = [1, 2, 3, 4]
    y_pred = [1, 2, 3, 4]
    metrics = regression_metrics(y_test, y_pred)
    assert "mae" in metrics
    assert "mse" in metrics
    assert "rmse" in metrics
    assert "r2" in metrics

def test_classification_metrics_perfect():
    """Test classification metrics with perfect predictions."""
    y_test = [0, 1, 0, 1]
    y_pred = [0, 1, 0, 1]
    y_prob = [0.1, 0.9, 0.2, 0.8]
    metrics = classification_metrics(y_test, y_pred, y_prob)
    assert metrics["accuracy"] == 1.0
