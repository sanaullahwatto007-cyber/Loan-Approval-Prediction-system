import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("loan_xgb_model.pkl")

st.title("Loan Approval Prediction System")

Applicant_Income = st.number_input("Applicant Income", min_value=0.0)
Coapplicant_Income = st.number_input("Coapplicant Income", min_value=0.0)
Marital_Status = st.selectbox("Marital Status", ["Single", "Married"])
Dependents = st.number_input("Dependents", min_value=0, step=1)
Credit_Score = st.number_input("Credit Score", min_value=0)
Existing_Loans = st.number_input("Existing Loans", min_value=0, step=1)
Age = st.number_input("Age", min_value=18, step=1)
DTI_Ratio = st.number_input("DTI Ratio", min_value=0.0)
Savings = st.number_input("Savings", min_value=0.0)
Collateral_Value = st.number_input("Collateral Value", min_value=0.0)
Loan_Amount = st.number_input("Loan Amount", min_value=0.0)
Loan_Term = st.number_input("Loan Term", min_value=0, step=1)

Loan_Purpose = st.selectbox(
    "Loan Purpose",
    ["Home", "Car", "Education", "Business", "Personal"]
)

Property_Area = st.selectbox(
    "Property Area",
    ["Urban", "Semiurban", "Rural"]
)

Education_Level = st.selectbox(
    "Education Level",
    ["Graduate", "Not Graduate"]
)

Gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

Employment_Status = st.selectbox(
    "Employment Status",
    ["Salaried", "Self-employed", "Contract", "Unemployed"]
)

Employer_Category = st.selectbox(
    "Employer Category",
    ["Private", "Government", "MNC", "Business", "Unemployed"]
)

if st.button("Predict Loan Approval"):

    input_data = pd.DataFrame([{
        "Applicant_Income": Applicant_Income,
        "Coapplicant_Income": Coapplicant_Income,
        "Marital_Status": Marital_Status,
        "Dependents": Dependents,
        "Credit_Score": Credit_Score,
        "Existing_Loans": Existing_Loans,
        "Age": Age,
        "DTI_Ratio": DTI_Ratio,
        "Savings": Savings,
        "Collateral_Value": Collateral_Value,
        "Loan_Amount": Loan_Amount,
        "Loan_Term": Loan_Term,
        "Loan_Purpose": Loan_Purpose,
        "Property_Area": Property_Area,
        "Education_Level": Education_Level,
        "Gender": Gender,
        "Employment_Status": Employment_Status,
        "Employer_Category": Employer_Category
    }])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Loan Approved ✅")
    else:
        st.error("Loan Not Approved ❌")