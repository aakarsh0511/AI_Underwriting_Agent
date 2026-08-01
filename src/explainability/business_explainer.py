class BusinessExplainer:

    def explain(self, application):

        row = application.iloc[0]

        positives = []

        negatives = []

        # ----------------------------
        # Income
        # ----------------------------

        if row["annual_inc"] >= 80000:

            positives.append(
                "Strong annual income."
            )

        else:

            negatives.append(
                "Annual income is relatively low."
            )

        # ----------------------------
        # Credit Score
        # ----------------------------

        if row["fico_range_low"] >= 740:

            positives.append(
                "Excellent credit score."
            )

        elif row["fico_range_low"] >= 700:

            positives.append(
                "Good credit score."
            )

        else:

            negatives.append(
                "Credit score is below preferred range."
            )

        # ----------------------------
        # Debt To Income
        # ----------------------------

        if row["dti"] <= 20:

            positives.append(
                "Debt-to-income ratio is healthy."
            )

        elif row["dti"] <= 35:

            negatives.append(
                "Debt-to-income ratio is moderately high."
            )

        else:

            negatives.append(
                "Debt-to-income ratio is high."
            )

        # ----------------------------
        # Credit Utilization
        # ----------------------------

        if row["revol_util"] <= 30:

            positives.append(
                "Credit utilization is low."
            )

        elif row["revol_util"] <= 60:

            negatives.append(
                "Credit utilization is moderate."
            )

        else:

            negatives.append(
                "Credit utilization is high."
            )

        # ----------------------------
        # Credit History
        # ----------------------------

        if row["credit_history_years"] >= 8:

            positives.append(
                "Long credit history."
            )

        else:

            negatives.append(
                "Limited credit history."
            )

        # ----------------------------
        # Enquiries
        # ----------------------------

        if row["inq_last_6mths"] <= 1:

            positives.append(
                "Few recent credit enquiries."
            )

        else:

            negatives.append(
                "Multiple recent credit enquiries."
            )

        return {

            "positives": positives,

            "negatives": negatives

        }