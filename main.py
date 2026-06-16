import streamlit as st
from prediction_helper import predict



st.title("Credit Risk Categorisation App")

col1, col2, col3 = st.columns(3)

with col1:
    loan_purpose = st.selectbox(
    "Please Select Loan Purpose: ", ["Business", "Home", "Personal", "Education"])
with col2:
    customer_age = st.number_input("Please Enter your Age: ")
with col3:
    customer_income = st.number_input("Please Enter your Annual Income: ")


col4, col5, col6 = st.columns(3)

with col4:
    customer_dependants = st.number_input("Please Enter your Dependants: ")
with col5:
    customer_year_current_address = st.number_input("Please Enter Years at Current Address: ")
with col6:
    residence_type = st.selectbox("Please Select Residence Type: ", ["Mortgage", "Owned","Rented"])

col7, col8, col9 = st.columns(3)

with col7:
    loan_type = st.selectbox("Please Select Loan Type: ", ["Secured", "Unsecured"])
with col8:
    loan_amount = st.number_input("Please Enter Loan Amount: ")
with col9:
    loan_tenure_months = st.number_input("Please Enter Loan Tenure (Months): ")

col10, col11, col12 = st.columns(3)

with col10:
    number_of_open_accounts = st.number_input("Please Enter Number of Open Accounts: ")
with col11:
    number_of_closed_accounts = st.number_input("Please Enter Number of Closed Accounts: ")
with col12:
    total_loan_months = st.number_input("Please Enter Total Loan Months: ")


col13, col14, col15 = st.columns(3)

with col13:
    total_dpd = st.number_input("Please Enter Total DPD: ")
with col14:
    enquiry_count = st.number_input("Please Enter Enquiry Count: ")
with col15:
    credit_utilization_ratio = st.number_input("Please Enter Credit Utilization Ratio: ")


input_dict = {
    "age": customer_age,
    "income": customer_income,
    "number_of_dependants": customer_dependants,
    "years_at_current_address": customer_year_current_address,
    "loan_amount": loan_amount,
    "loan_tenure_months": loan_tenure_months,
    "number_of_open_accounts": number_of_open_accounts,
    "number_of_closed_accounts": number_of_closed_accounts,
    "total_loan_months": total_loan_months,
    "total_dpd": total_dpd,
    "enquiry_count": enquiry_count,
    "credit_utilization_ratio": credit_utilization_ratio,

    "loan_purpose": loan_purpose,

    "residence_type": residence_type,


    "loan_type": loan_type
}


st.markdown("---")

if st.button("Check Loan Approval"):

    message, confidence = predict(input_dict)

    st.subheader("Prediction Result")

    if confidence > 0.8:
        st.success(message)
    else:
        st.warning(message)

    st.write(f"Confidence Score: {confidence:.2%}")





