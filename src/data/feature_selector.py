import pandas as pd


class FeatureSelector:

    """
    Select only the columns that would be available
    to an underwriter before loan approval.
    """

    def __init__(self):

        self.target = "loan_status"

        self.selected_features = [

            # Loan Information
            "loan_amnt",
            "term",
            "int_rate",
            "purpose",

            # Customer Information
            "emp_length",
            "home_ownership",
            "annual_inc",
            "verification_status",

            # Credit Information
            "dti",
            "fico_range_low",
            "fico_range_high",
            "inq_last_6mths",
            "open_acc",
            "pub_rec",
            "revol_bal",
            "revol_util",
            "total_acc",

            # Engineered Features
            "monthly_income",
            "loan_to_income_ratio",
            "installment_income_ratio",
            "credit_history_years",
            "total_credit_exposure"
        ]

    def transform(self, df):

        available_features = [
            col
            for col in self.selected_features
            if col in df.columns
        ]

        selected_columns = available_features + [self.target]

        return df[selected_columns]