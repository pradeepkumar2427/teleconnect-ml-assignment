from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

def train_logistic_regression(X_train, y_train):
    """Train Logistic Regression."""
    param_grid = {"C": [0.1, 1, 10]}
    grid = GridSearchCV(LogisticRegression(max_iter=1000), param_grid, cv=3)
    grid.fit(X_train, y_train)
    return grid.best_estimator_

def train_decision_tree(X_train, y_train):
    """Train Decision Tree."""
    param_grid = {"max_depth": [3, 5, 10]}
    grid = GridSearchCV(DecisionTreeClassifier(random_state=42), param_grid, cv=3)
    grid.fit(X_train, y_train)
    return grid.best_estimator_

def train_random_forest(X_train, y_train):
    """Train Random Forest."""
    param_grid = {"n_estimators": [50, 100], "max_depth": [5, 10]}
    grid = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=3)
    grid.fit(X_train, y_train)
    return grid.best_estimator_

def train_svm(X_train, y_train):
    """Train SVM."""
    param_grid = {"C": [0.1, 1]}
    grid = GridSearchCV(SVC(probability=True, kernel="linear"), param_grid, cv=3)
    grid.fit(X_train, y_train)
    return grid.best_estimator_

def train_knn(X_train, y_train):
    """Train KNN."""
    param_grid = {"n_neighbors": [3, 5]}
    grid = GridSearchCV(KNeighborsClassifier(), param_grid, cv=3)
    grid.fit(X_train, y_train)
    return grid.best_estimator_
