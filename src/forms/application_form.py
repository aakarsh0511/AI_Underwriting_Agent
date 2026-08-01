import streamlit as st
import pandas as pd


class CustomerApplicationForm:

    def render(self):

        st.subheader("Customer Loan Application")

        loan_amnt = st.number_input(
            "Loan Amount",
            min_value=1000.0,
            value=100000.0
        )

        term = st.selectbox(
            "Loan Term",
            [
                " 36 months",
                " 60 months"
            ]
        )

        int_rate = st.number_input(
            "Interest Rate (%)",
            min_value=1.0,
            max_value=40.0,
            value=12.0
        )

        purpose = st.selectbox(
            "Loan Purpose",
            [
                "debt_consolidation",
                "credit_card",
                "home_improvement",
                "major_purchase",
                "small_business",
                "medical",
                "vacation",
                "car",
                "house",
                "moving",
                "renewable_energy",
                "other"
            ]
        )

        emp_length = st.selectbox(
            "Employment Length",
            [
                "< 1 year",
                "1 year",
                "2 years",
                "3 years",
                "4 years",
                "5 years",
                "6 years",
                "7 years",
                "8 years",
                "9 years",
                "10+ years"
            ]
        )

        home_ownership = st.selectbox(
            "Home Ownership",
            [
                "RENT",
                "OWN",
                "MORTGAGE",
                "OTHER"
            ]
        )

        annual_inc = st.number_input(
            "Annual Income",
            min_value=0.0,
            value=600000.0
        )

        verification_status = st.selectbox(
            "Income Verification",
            [
                "Verified",
                "Source Verified",
                "Not Verified"
            ]
        )

        dti = st.number_input(
            "Debt To Income Ratio",
            min_value=0.0,
            value=15.0
        )

        fico_range_low = st.number_input(
            "FICO Low",
            min_value=300,
            max_value=900,
            value=700
        )

        fico_range_high = st.number_input(
            "FICO High",
            min_value=300,
            max_value=900,
            value=704
        )

        inq_last_6mths = st.number_input(
            "Credit Enquiries (Last 6 Months)",
            min_value=0,
            value=1
        )

        open_acc = st.number_input(
            "Open Accounts",
            min_value=0,
            value=8
        )

        pub_rec = st.number_input(
            "Public Records",
            min_value=0,
            value=0
        )

        revol_bal = st.number_input(
            "Revolving Balance",
            min_value=0.0,
            value=25000.0
        )

        revol_util = st.number_input(
            "Credit Utilization (%)",
            min_value=0.0,
            max_value=100.0,
            value=35.0
        )

        total_acc = st.number_input(
            "Total Accounts",
            min_value=0,
            value=20
        )

        credit_history_years = st.number_input(
            "Credit History (Years)",
            min_value=0.0,
            value=10.0
        )

        if st.button("Analyze Application"):

            monthly_income = annual_inc / 12

            loan_to_income_ratio = loan_amnt / (annual_inc + 1)

            installment = loan_amnt / 36

            installment_income_ratio = installment / (
                monthly_income + 1
            )

            total_credit_exposure = (
                loan_amnt +
                revol_bal
            )

            return pd.DataFrame([{

                "loan_amnt": loan_amnt,
                "term": term,
                "int_rate": int_rate,
                "purpose": purpose,
                "emp_length": emp_length,
                "home_ownership": home_ownership,
                "annual_inc": annual_inc,
                "verification_status": verification_status,
                "dti": dti,
                "fico_range_low": fico_range_low,
                "fico_range_high": fico_range_high,
                "inq_last_6mths": inq_last_6mths,
                "open_acc": open_acc,
                "pub_rec": pub_rec,
                "revol_bal": revol_bal,
                "revol_util": revol_util,
                "total_acc": total_acc,
                "monthly_income": monthly_income,
                "loan_to_income_ratio": loan_to_income_ratio,
                "installment_income_ratio": installment_income_ratio,
                "credit_history_years": credit_history_years,
                "total_credit_exposure": total_credit_exposure

            }])

        return None