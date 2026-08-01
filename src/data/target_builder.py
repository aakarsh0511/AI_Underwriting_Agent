class TargetBuilder:
    """
    Creates the binary target variable for underwriting.

    Good Loan (0)  -> Fully Paid
    Bad Loan (1)   -> Charged Off
    """

    def __init__(self):

        self.valid_status = {
            "Fully Paid": 0,
            "Charged Off": 1
        }

    def transform(self, df):

        df = df.copy()

        # Keep only valid loan statuses
        df = df[
            df["loan_status"].isin(self.valid_status.keys())
        ].copy()

        # Create binary target
        df["loan_status"] = df["loan_status"].map(
            self.valid_status
        )

        return df