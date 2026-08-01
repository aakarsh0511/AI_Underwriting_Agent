class LoanOptimizer:

    def optimize(self, application):

        row = application.iloc[0]

        suggestions = []

        # ---------------------------------------------------
        # Loan Amount Recommendation
        # ---------------------------------------------------

        recommended_loan = row["annual_inc"] * 0.50

        if row["loan_amnt"] > recommended_loan:

            suggestions.append({

                "Category": "Loan Amount",

                "Current": f"₹{row['loan_amnt']:,.0f}",

                "Suggested": f"₹{recommended_loan:,.0f}",

                "Benefit": "Lower loan-to-income ratio and lower default risk."

            })

        # ---------------------------------------------------
        # DTI
        # ---------------------------------------------------

        if row["dti"] > 30:

            suggestions.append({

                "Category": "Debt-to-Income Ratio",

                "Current": f"{row['dti']:.1f}%",

                "Suggested": "< 30%",

                "Benefit": "Improves repayment affordability."

            })

        # ---------------------------------------------------
        # Credit Utilization
        # ---------------------------------------------------

        if row["revol_util"] > 60:

            suggestions.append({

                "Category": "Credit Utilization",

                "Current": f"{row['revol_util']:.1f}%",

                "Suggested": "< 30%",

                "Benefit": "Lower utilization generally indicates stronger credit health."

            })

        # ---------------------------------------------------
        # Credit Score
        # ---------------------------------------------------

        if row["fico_range_low"] < 700:

            suggestions.append({

                "Category": "Credit Score",

                "Current": row["fico_range_low"],

                "Suggested": "700+",

                "Benefit": "Higher score generally improves approval chances."

            })

        # ---------------------------------------------------
        # Credit History
        # ---------------------------------------------------

        if row["credit_history_years"] < 5:

            suggestions.append({

                "Category": "Credit History",

                "Current": f"{row['credit_history_years']:.1f} Years",

                "Suggested": "Add Co-Applicant",

                "Benefit": "Additional applicant can strengthen the application."

            })

        return suggestions