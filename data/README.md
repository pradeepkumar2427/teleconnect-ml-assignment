# Data Dictionary

## Source
Telco Customer Churn dataset from Kaggle:
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

## Raw Data
Tele-Customer-Churn.csv: Original dataset with 7043 rows and 21 features

## Features
- customerID: Unique identifier
- gender: Male/Female
- SeniorCitizen: 0 or 1
- Partner: Yes/No
- Dependents: Yes/No
- tenure: Months with company
- MonthlyCharges: Monthly charge amount
- TotalCharges: Total charges to date
- Churn: Yes/No Target

## Processed Data
- cleaned_data.csv: Cleaned data after EDA
- X_train.csv, X_val.csv, X_test.csv: Feature splits
- y_train.csv, y_val.csv, y_test.csv: Target splits
