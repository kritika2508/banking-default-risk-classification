# Banking Customer Default Risk Classification

> **Academic project | Business Analytics + Machine Learning**

A classification-based banking analytics project exploring whether customer and banking attributes can be used to identify customers associated with loan-default outcomes.

## Business Context

This academic project asks:

**Can available customer and banking attributes help identify customers with a higher observed likelihood of default?**

The objective is to demonstrate how a business risk question can be translated into a classification problem and evaluated using risk-oriented metrics.

## Business Questions

1. Which customer and banking attributes are associated with default outcomes?
2. How severe is the class imbalance in the target?
3. Which classification approaches identify default cases most effectively?
4. What is the trade-off between identifying defaulters and incorrectly flagging non-defaulters?
5. Which metrics should a business team monitor before considering further validation?

## Dataset

- **Rows:** 255,265
- **Features:** 15 input attributes plus target
- **Target:** `DefaulterYN`
- **Target distribution:** approximately 99.1% `No` and 0.9% `Yes`

The original academic dataset contains customer/account attributes such as customer type, branch, customer category, gender, location, risk grade, income, account counts, loan-account count and education.

> **Data note:** The original customer-level CSV is intentionally not committed to this public repository. The project is structured so the notebook can be run locally after placing the dataset at `data/Banking.csv`. Do not publish sensitive or non-public customer data.

## Analytical Workflow

```
Business Problem
      ↓
Data Understanding
      ↓
Data Quality Checks
      ↓
Missing-value Treatment
      ↓
Duplicate / Low-information Treatment
      ↓
Feature Engineering
      ↓
Categorical Encoding
      ↓
Class Imbalance Treatment
      ↓
Train / Test Split
      ↓
Model Development
      ↓
Model Comparison
      ↓
Business Interpretation
```

## Data Preparation

The preprocessing workflow includes:

- Duplicate removal
- Missing-value thresholding
- Missing-value treatment using mode/median
- Low-information treatment
- Numerical feature bucketing
- Label encoding
- Minority-class resampling

## Models Evaluated

- Logistic Regression
- K-Nearest Neighbors
- Decision Tree
- Random Forest
- AdaBoost
- Gradient Boosting

## Evaluation Framework

Because default is a rare outcome, **accuracy alone is insufficient**.

| Metric | Business interpretation |
|---|---|
| Accuracy | Overall classification correctness |
| Recall | How many actual defaulters were identified |
| Precision | How many predicted defaulters were actually defaulters |
| F1 Score | Balance between precision and recall |
| Confusion Matrix | Operational view of false positives and false negatives |

For a risk-screening workflow, recall and precision should be considered together because false negatives and false positives have different business consequences.

## Business Analysis Perspective

A practical decision workflow would look like:

```
Customer Data
     ↓
Risk Model
     ↓
Risk Probability / Classification
     ↓
Human Review / Policy Rules
     ↓
Lending Decision
     ↓
Monitoring & Model Validation
```

A production implementation would require additional work, including probability calibration, threshold optimization, out-of-time validation, explainability, fairness assessment, drift monitoring, governance and regulatory review.

## Key Academic Learning

The project demonstrates how to move from a highly imbalanced business classification problem to a structured modelling workflow while considering the **business cost of model errors**, rather than treating accuracy as the only objective.

## Repository Structure

```
banking-default-risk-classification/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── notebooks/
│   └── Banking_classification.ipynb
│
├── src/
│   └── data_preprocessing.py
│
└── docs/
    ├── business_context.md
    ├── model_evaluation.md
    └── limitations.md
```

## Technology Stack

`Python` · `Pandas` · `NumPy` · `Scikit-learn` · `Plotly` · `Jupyter Notebook`

## Disclaimer

This is an academic project based on an analytical dataset. It is **not a production credit-scoring or lending-decision system**. Real-world deployment would require appropriate validation, explainability, fairness, privacy, regulatory and governance controls.
