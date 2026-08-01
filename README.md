# AI Underwriting Agent

> **An end-to-end AI-powered underwriting decision support system that transforms machine learning predictions into business-friendly lending insights.**

---

# Problem Statement

Financial institutions process thousands of loan applications every day. While machine learning models can estimate the **Probability of Default (PD)**, a prediction alone is rarely enough for making a lending decision.

Underwriters need answers to questions such as:

- Is this applicant risky?
- How confident is the prediction?
- Which financial factors influenced the decision?
- Why should this loan be approved or reviewed?

Most machine learning projects stop after displaying a prediction score, leaving the interpretation to the underwriter.

This project addresses that gap by building an **AI Underwriting Agent** that combines machine learning with business-oriented risk intelligence, making credit decisions more transparent, explainable, and actionable.

---

# Our Approach

Instead of treating credit risk prediction as a standalone machine learning problem, this project models the complete underwriting workflow.

The system first trains a machine learning model using historical lending data. During deployment, an underwriter enters a new customer's financial information through an application form. The platform automatically performs feature engineering, preprocesses the inputs, generates a probability of default, translates the prediction into business-friendly risk metrics, and explains the major financial strengths and weaknesses of the applicant.

The objective is not simply to predict whether a customer may default, but to provide meaningful insights that help an underwriter make informed lending decisions.

---

# Solution Workflow

## Offline Training Pipeline

```text
Historical Lending Dataset
            │
            ▼
     Data Cleaning & EDA
            │
            ▼
    Feature Engineering
            │
            ▼
      Preprocessing
            │
            ▼
      Model Training
            │
            ▼
     Model Evaluation
            │
            ▼
 Save Model + Preprocessor
```

## Online AI Underwriting Agent

```text
Customer Application Form
            │
            ▼
     Input Validation
            │
            ▼
 Automatic Feature Engineering
            │
            ▼
 Load Preprocessor + Model
            │
            ▼
     Risk Prediction
            │
            ▼
    Risk Intelligence
            │
            ▼
 Business Explainability
```

---

# Key Features

### Offline Machine Learning Pipeline

- Historical lending data preprocessing
- Automated data cleaning
- Business-oriented feature engineering
- Feature selection
- Binary target creation (Good Loan vs Bad Loan)
- Train-Test Split
- Data preprocessing pipeline
- Multiple model training
- Best model selection
- Model persistence using Joblib

---

### Online AI Underwriting Agent

- Customer loan application form
- Automatic business feature generation
- Probability of Default (PD) prediction
- Risk Score generation
- Risk Bucket classification
- Prediction confidence
- Business-friendly explainability
- Lending recommendation

---

# Business Feature Engineering

The platform derives business-focused financial metrics that better represent customer affordability and repayment capacity.

Engineered features include:

- Monthly Income
- Loan-to-Income Ratio
- Installment-to-Income Ratio
- Credit History (Years)
- Total Credit Exposure

These features provide richer financial information than the original dataset alone.

---

# Risk Intelligence

Instead of displaying raw model outputs, the platform converts predictions into business-friendly underwriting metrics.

Example:

| Metric | Example |
|---------|---------|
| Probability of Default | 14% |
| Risk Score | 860 / 1000 |
| Risk Bucket | Low |
| Recommendation | Approve |

---

# Business Explainability

Instead of presenting technical feature importance values, the platform explains the decision using underwriting terminology.

### Positive Factors

- Strong annual income
- Healthy debt-to-income ratio
- Good credit score
- Long credit history

### Risk Factors

- High credit utilization
- Moderate debt burden

This allows business users to understand the reasoning behind every prediction.

---

# Project Structure

```text
AI_Underwriting_Agent/
│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   ├── best_model.pkl
│   └── preprocessor.pkl
│
├── src/
│   ├── data/
│   ├── preprocessing/
│   ├── models/
│   ├── pipeline/
│   ├── forms/
│   ├── explainability/
│   └── risk/
```

---

# Technology Stack

## Programming Language

- Python

## Machine Learning

- Scikit-learn
- Logistic Regression
- Random Forest

## Data Processing

- Pandas
- NumPy

## Model Persistence

- Joblib

## Frontend

- Streamlit

## Visualization

- Plotly
- Matplotlib

---



# Why This Project?

Most credit risk projects stop after predicting whether a customer may default.

This project focuses on **underwriting decision intelligence**, transforming machine learning predictions into business-friendly insights that help underwriters understand risk, interpret model outputs, and make more informed lending decisions.

The goal is not just to predict risk—but to support better credit decisions.
