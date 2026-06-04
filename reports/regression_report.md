# Regression Report
## Best Model: Linear Regression

## Why Linear Regression is Best
- No overfitting (train and test R2 almost same)
- Lowest MAE and RMSE on test data
- MonthlyCharges has linear relationship with features
- Simple and interpretable for business use

## Results Summary
| Model | MAE | MSE | RMSE | R2 |
|-------|-----|-----|------|----|
| Linear Regression | 0.79 | 1.11 | 1.05 | 0.9988 |
| Ridge | 0.79 | 1.11 | 1.05 | 0.9988 |
| Lasso | 0.79 | 1.10 | 1.05 | 0.9988 |
| ElasticNet | 0.79 | 1.11 | 1.05 | 0.9988 |
| Decision Tree | 0.98 | 1.96 | 1.40 | 0.9978 |
| Random Forest | 1.50 | 4.34 | 2.08 | 0.9952 |
| SVR | 0.79 | 1.11 | 1.05 | 0.9988 |

## Why Same Values for Linear Models
Linear Regression, Ridge, Lasso and ElasticNet gave same results because:
- Data has clean linear relationship
- No multicollinearity issues
- Regularization not needed for this dataset
- All converge to same solution
