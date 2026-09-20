import streamlit as st
import pandas as pd
import joblib

model = joblib.load("LoanModel.pkl")

st.title("Loan Approval Prediction")

income = st.number_input(
    "Enter the Income",
    min_value=0.0,
    value=50000.0,
    step=1000.0
)
credit_score = st.number_input(
    "Enter the Credit Score",
    min_value=0.0,
    value=720.0,
    step=1.0
)
if st.button("Predict"):

    input_data = pd.DataFrame({
        "Income": [income],
        "Credit_Score": [credit_score]
    })
    prediction = model.predict(input_data)
    pred = prediction[0]
    if pred == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Not Approved")
