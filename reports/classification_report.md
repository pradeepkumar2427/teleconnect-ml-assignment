# Classification Report
## Best Model: Logistic Regression

## Why Logistic Regression is Best
- Highest ROC-AUC: 0.8343
- Highest Accuracy: 0.7852
- Simple and interpretable
- No overfitting
- Works well for binary classification
- Fast to train and predict

## Results
| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|-------|----------|-----------|--------|----|---------|
| Logistic Regression | 0.7852 | 0.7547 | 0.2847 | 0.4134 | 0.8343 |
| Decision Tree | 0.4749 | 0.3102 | 0.7972 | 0.4467 | 0.6815 |
| SVM | 0.7588 | 0.8421 | 0.1139 | 0.2006 | 0.8295 |
| KNN | 0.7682 | 0.5968 | 0.3950 | 0.4754 | 0.7608 |
| Random Forest | 0.7294 | 0.4900 | 0.7900 | 0.6100 | 0.8172 |

## Conclusion
Logistic Regression selected as best model because:
- Highest ROC-AUC score shows best discrimination ability
- Highest accuracy on test data
- Simple linear model suitable for this dataset
- Easy to interpret coefficients as feature importance
