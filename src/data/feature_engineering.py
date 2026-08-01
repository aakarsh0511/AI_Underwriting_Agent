import pandas as pd
import numpy as np


class FeatureEngineer:

    def transform(self, df):

        df = df.copy()

        # -------------------------
        # Monthly Income
        # -------------------------

        if "annual_inc" in df.columns:
            df["monthly_income"] = df["annual_inc"] / 12

        # -------------------------
        # Loan to Income Ratio
        # -------------------------

        if {"loan_amnt", "annual_inc"}.issubset(df.columns):

            df["loan_to_income_ratio"] = (
                df["loan_amnt"] /
                (df["annual_inc"] + 1)
            )

        # -------------------------
        # Installment to Income Ratio
        # -------------------------

        if {"installment", "monthly_income"}.issubset(df.columns):

            df["installment_income_ratio"] = (
                df["installment"] /
                (df["monthly_income"] + 1)
            )

        # -------------------------
        # Credit Utilization
        # -------------------------

        if "revol_util" in df.columns:

            df["revol_util"] = (
                df["revol_util"]
                .astype(str)
                .str.replace("%", "", regex=False)
            )

            df["revol_util"] = pd.to_numeric(
                df["revol_util"],
                errors="coerce"
            )

        # -------------------------
        # Credit History Length
        # -------------------------

        if "earliest_cr_line" in df.columns:

            df["earliest_cr_line"] = pd.to_datetime(
                df["earliest_cr_line"],
                format="%b-%y",
                errors="coerce"
            )

            current_date = pd.Timestamp.today()

            df["credit_history_years"] = (
                (
                    current_date -
                    df["earliest_cr_line"]
                ).dt.days / 365
            )

        # -------------------------
        # Total Credit Exposure
        # -------------------------

        if {"revol_bal", "loan_amnt"}.issubset(df.columns):

            df["total_credit_exposure"] = (
                df["revol_bal"] +
                df["loan_amnt"]
            )

        return df