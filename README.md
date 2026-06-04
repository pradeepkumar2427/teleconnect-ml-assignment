# TeleConnect ML Assignment
Customer Churn Prediction and Revenue Forecasting using Supervised Learning.
Built as part of ML Engineer recruitment assignment at TeleConnect Telecom Company.

## Dataset
Telco Customer Churn dataset from Kaggle:
https://www.kaggle.com/datasets/blastchar/telco-customer-churn
7043 customer records with 21 features.

## Installation and Setup
git clone https://github.com/pradeepkumar2427/teleconnect-ml-assignment.git
cd teleconnect-ml-assignment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## How to Run
1. Run notebooks/01_EDA.ipynb
2. Run notebooks/02_preprocessing.ipynb
3. Run notebooks/03_classification.ipynb
4. Run notebooks/04_regression.ipynb
5. Run notebooks/05_interpretation.ipynb

## Results Summary
- Best Classifier: Random Forest
- Best Regressor: Linear Regression (R2: 0.9988)
- Key Insight: Contract type and tenure are top churn drivers

## Project Architecture
teleconnect-ml-assignment/
├── data/raw/
├── data/processed/
├── notebooks/
├── src/
├── models/
├── reports/
└── tests/

## Tech Stack
- pandas: data manipulation
- numpy: numerical computing
- scikit-learn: machine learning
- matplotlib/seaborn: visualizations
- shap: model interpretation
- imbalanced-learn: class imbalance
- joblib: model saving
