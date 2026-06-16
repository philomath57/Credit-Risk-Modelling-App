import streamlit as st
import pandas as pd
import joblib


model = joblib.load("Risk_Modelling_Results/lightgbm.joblib")
scale = joblib.load("Risk_Modelling_Results/scale.joblib")

def prepare_data(input_dict):

    data = {
        "age": input_dict["age"],
        "income": input_dict["income"],
        "number_of_dependants": input_dict["number_of_dependants"],
        "years_at_current_address": input_dict["years_at_current_address"],
        "loan_amount": input_dict["loan_amount"],
        "loan_tenure_months": input_dict["loan_tenure_months"],
        "number_of_open_accounts": input_dict["number_of_open_accounts"],
        "number_of_closed_accounts": input_dict["number_of_closed_accounts"],
        "total_loan_months": input_dict["total_loan_months"],
        "total_dpd": input_dict["total_dpd"],
        "enquiry_count": input_dict["enquiry_count"],
        "credit_utilization_ratio": input_dict["credit_utilization_ratio"],

        "loan_purpose_Education": 1 if input_dict["loan_purpose"] == "Education" else 0,
        "loan_purpose_Home": 1 if input_dict["loan_purpose"] == "Home" else 0,
        "loan_purpose_Personal": 1 if  input_dict["loan_purpose"] == "Personal" else 0,

        "residence_type_Owned": 1 if input_dict["residence_type"] == "Owned" else 0,
        "residence_type_Rented": 1 if input_dict["residence_type"] == "Rented" else 0,


        "loan_type_Unsecured": 1 if input_dict["loan_type"] == "Unsecured" else 0
    }

    data = pd.DataFrame([data])

    num_cols = [
    "age",
    "income",
    "number_of_dependants",
    "years_at_current_address",
    "loan_amount",
    "loan_tenure_months",
    "number_of_open_accounts",
    "number_of_closed_accounts",
    "total_loan_months",
    "total_dpd",
    "enquiry_count",
    "credit_utilization_ratio"]
    
    data[num_cols] = scale.transform(data[num_cols])

    expected_columns = [
    'age',
    'income',
    'number_of_dependants',
    'years_at_current_address',
    'loan_amount',
    'loan_tenure_months',
    'number_of_open_accounts',
    'number_of_closed_accounts',
    'total_loan_months',
    'total_dpd',
    'enquiry_count',
    'credit_utilization_ratio',
    'loan_purpose_Education',
    'loan_purpose_Home',
    'loan_purpose_Personal',
    'residence_type_Owned',
    'residence_type_Rented',
    'loan_type_Unsecured'
]
    
    data = data[expected_columns]

    return data

def predict(input_dict):

    input_df = prepare_data(input_dict)

    prediction = model.predict(input_df)[0]
    probs = model.predict_proba(input_df)[0]

    if prediction == 0:
        return (
            "Customer is having a convincing record and hence loan can be granted",
            probs[0]
        )
    else:
        return (
            "Customer is not having a convincing record and there are high chances of default",
            probs[1]
        )
