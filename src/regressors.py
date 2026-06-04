from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV

def train_linear_regression(X_train, y_train):
    """Train Linear Regression."""
    param_grid = {"fit_intercept": [True, False]}
    grid = GridSearchCV(LinearRegression(), param_grid, cv=3)
    grid.fit(X_train, y_train)
    return grid.best_estimator_

def train_ridge(X_train, y_train):
    """Train Ridge Regression."""
    param_grid = {"alpha": [0.01, 0.1, 1, 10]}
    grid = GridSearchCV(Ridge(), param_grid, cv=3)
    grid.fit(X_train, y_train)
    return grid.best_estimator_

def train_random_forest(X_train, y_train):
    """Train Random Forest Regressor."""
    param_grid = {"n_estimators": [50, 100], "max_depth": [5, 10]}
    grid = GridSearchCV(RandomForestRegressor(random_state=42), param_grid, cv=3)
    grid.fit(X_train, y_train)
    return grid.best_estimator_
