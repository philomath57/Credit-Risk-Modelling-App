# Credit Risk Modelling and Fairness-Aware Loan Default Prediction Using LightGBM

## Overview

This project presents an end-to-end machine learning solution for predicting the likelihood of loan default using customer demographic, financial, and credit behaviour information. The system employs a LightGBM classifier trained on historical credit data and is deployed as an interactive Streamlit web application.

Beyond predictive performance, the project incorporates Responsible AI principles by evaluating model fairness across different age groups. Explainable AI techniques using SHAP (SHapley Additive Explanations) are also employed to improve transparency and interpretability of model predictions.

The objective of this project is to assist financial institutions in identifying high-risk loan applicants while promoting fair, transparent, and data-driven lending decisions.

---

## Key Features

- Loan default prediction using Machine Learning
- Real-time risk assessment through a Streamlit web application
- Automated data preprocessing and feature engineering
- LightGBM-based classification model
- Probability-based risk prediction
- SHAP-based model explainability
- Fairness analysis using Fairlearn
- Responsible AI-focused credit risk assessment
- User-friendly interface for credit analysts and lending institutions

---

## Machine Learning Pipeline

### Data Preprocessing

The following preprocessing steps were performed:

- Data cleaning and validation
- One-hot encoding of categorical variables
- Feature scaling using MinMaxScaler
- Train-test split
- Handling class imbalance through class weighting

### Features Used

#### Customer Information

- Age
- Annual Income
- Number of Dependants
- Years at Current Address

#### Loan Information

- Loan Purpose
- Loan Amount
- Loan Tenure
- Loan Type

#### Credit Behaviour Information

- Number of Open Accounts
- Number of Closed Accounts
- Total Loan Months
- Total Days Past Due (DPD)
- Enquiry Count
- Credit Utilization Ratio

---

## Model Development

### Algorithm

The final predictive model was developed using:

- LightGBM Classifier

### Model Evaluation Metrics

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score
- Confusion Matrix

### Classification Results

| Class | Precision | Recall | F1-Score |
|---------|---------|---------|---------|
| Non-Default (0) | 1.00 | 0.93 | 0.96 |
| Default (1) | 0.55 | 0.95 | 0.70 |

### Overall Performance

| Metric | Score |
|----------|----------|
| Accuracy | 93% |
| Weighted F1 Score | 94% |
| Recall (Default Class) | 95% |

### Key Findings

The model successfully identifies 95% of actual defaulters, making it highly effective for credit risk screening. Although precision for the default class is comparatively lower (55%), the model intentionally prioritises recall to minimise the risk of approving potentially high-risk borrowers.

This approach aligns with real-world lending practices where missing a genuine defaulter can be significantly more costly than incorrectly flagging a low-risk applicant.

---

## Explainable AI (SHAP Analysis)

To improve transparency and interpretability, SHAP (SHapley Additive Explanations) was applied to understand the factors driving model predictions.

### Most Influential Features

1. Credit Utilization Ratio
2. Total Days Past Due (DPD)
3. Loan Purpose
4. Total Loan Months
5. Residence Type
6. Enquiry Count
7. Age
8. Income

### Key Insights

#### Credit Utilization Ratio

Credit Utilization Ratio emerged as the most influential feature. Higher utilization levels consistently increased the probability of default, indicating that excessive use of available credit is strongly associated with financial stress and repayment difficulties.

#### Total Days Past Due (DPD)

Historical delinquency records significantly increased default risk. Customers with higher DPD values were substantially more likely to be classified as high-risk borrowers.

#### Loan Purpose

Home and Education-related loans showed moderate influence on model decisions, suggesting that borrowing objectives can impact repayment behaviour.

#### Total Loan Months

Longer borrowing histories generally reduced predicted default risk, indicating that established credit relationships may reflect greater financial stability.

#### Residence Type

Customers living in rented accommodation exhibited higher predicted risk, while property ownership was associated with lower default probability.

#### Age and Income

Although age and income contributed to predictions, their influence was considerably smaller than behavioural credit indicators, suggesting that model decisions are primarily driven by financial behaviour rather than demographic characteristics.

---

## Fairness Analysis

To support Responsible AI principles, fairness analysis was conducted using age group as a sensitive attribute.

### Age Groups Evaluated

- Under 25
- 25–40
- 41–60
- Above 60

### Fairness Metrics

The following fairness metrics were assessed:

- Demographic Parity (Selection Rate)
- Equal Opportunity (True Positive Rate)
- False Positive Rate Comparison
- Group-wise Performance Analysis

### Results

| Age Group | Selection Rate | True Positive Rate (TPR) | False Positive Rate (FPR) |
|------------|------------|------------|------------|
| Under 25 | 0.164 | 0.900 | 0.072 |
| 25–40 | 0.161 | 0.962 | 0.079 |
| 41–60 | 0.125 | 0.950 | 0.063 |
| Above 60 | 0.084 | 1.000 | 0.041 |

### Fairness Interpretation

#### Demographic Parity

Selection rates vary across age groups, with younger customers being classified as potential defaulters more frequently than older customers. This indicates that perfect demographic parity is not achieved.

#### Equal Opportunity

The model achieves consistently high True Positive Rates across all age groups, ranging from 90% to 100%. This suggests that actual defaulters are identified effectively regardless of age category.

#### False Positive Rate Analysis

False Positive Rates remain relatively consistent across groups, ranging between 4.1% and 7.9%, indicating that no age group is disproportionately subjected to incorrect default predictions.

### Overall Fairness Assessment

The fairness analysis suggests that while demographic parity is not fully achieved, the model demonstrates strong Equal Opportunity characteristics and balanced False Positive Rates.

Combined with the SHAP findings, the results indicate that model decisions are primarily driven by financial behaviour and repayment history rather than demographic attributes alone.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- LightGBM
- Fairlearn
- SHAP
- Joblib
- Streamlit

---

## Project Structure

```text
Credit-Risk-Modelling-App/
│
├── main.py
├── prediction_helper.py
├── requirements.txt
├── README.md
│
├── Risk_Modelling_Results/
│   ├── lightgbm.joblib
│   └── scale.joblib
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/philomath57/Credit-Risk-Modelling-App.git
```

### Navigate to Project Directory

```bash
cd Credit-Risk-Modelling-App
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run main.py
```

---

## Application Workflow

1. Enter customer demographic details.
2. Enter loan-related information.
3. Enter credit behaviour metrics.
4. Click **Check Loan Approval**.
5. Receive:
   - Default prediction
   - Confidence score
   - Loan risk assessment

---

## Future Enhancements

- SHAP visualisation dashboard within the web application
- Individual prediction explanations
- Risk categorisation (Low, Medium, High)
- PDF report generation
- Additional fairness metrics
- Bias mitigation techniques
- Model monitoring and drift detection
- Cloud deployment with CI/CD integration

---

## Disclaimer

This project has been developed for academic and research purposes. Predictions generated by the model should not be used as the sole basis for real-world lending decisions. Financial institutions should combine model outputs with domain expertise, regulatory requirements, and comprehensive credit assessment procedures.

---
