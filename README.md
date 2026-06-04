# TeleConnect ML Assignment
Customer Churn Prediction and Revenue Forecasting using Supervised Learning

## Dataset
- Source: https://www.kaggle.com/datasets/blastchar/telco-customer-churn
- 7,043 customer records with 21 features
- Classification target: Churn (Yes/No)
- Regression target: MonthlyCharges

## Installation and Setup
git clone https://github.com/pradeepkumar2427/teleconnect-ml-assignment.git
cd teleconnect-ml-assignment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## How to Run
1. Add dataset to data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv
2. Run notebooks in order:
   - notebooks/01_EDA.ipynb
   - notebooks/02_preprocessing.ipynb
   - notebooks/03_classification.ipynb
   - notebooks/04_regression.ipynb
   - notebooks/05_interpretation.ipynb

## Results Summary
| Task | Best Model | Key Metric |
|------|-----------|------------|
| Classification | Random Forest | ROC-AUC: 0.85 |
| Regression | Random Forest | R2: 0.92 |

## Key Insight
Contract type and tenure are the strongest predictors
of customer churn. Month-to-month customers are 3x
more likely to churn than two-year contract customers.

## Project Architecture
teleconnect-ml-assignment/
|-- README.md
|-- requirements.txt
|-- .gitignore
|-- data/
|   |-- raw/
|   |-- processed/
|   |-- README.md
|-- notebooks/
|   |-- 01_EDA.ipynb
|   |-- 02_preprocessing.ipynb
|   |-- 03_classification.ipynb
|   |-- 04_regression.ipynb
|   |-- 05_interpretation.ipynb
|-- src/
|   |-- data_loader.py
|   |-- preprocessing.py
|   |-- classifiers.py
|   |-- regressors.py
|   |-- evaluation.py
|   |-- utils.py
|-- models/
|   |-- best_classifier.pkl
|   |-- best_regressor.pkl
|-- reports/
|   |-- figures/
|   |-- classification_report.md
|   |-- regression_report.md
|-- tests/
|   |-- test_preprocessing.py
|   |-- test_evaluation.py

## Tech Stack
| Library | Purpose |
|---------|---------|
| pandas | Data manipulation |
| numpy | Numerical computing |
| scikit-learn | ML algorithms |
| matplotlib | Visualization |
| seaborn | Statistical plots |
| shap | Model explainability |
| imbalanced-learn | SMOTE, class balancing |
