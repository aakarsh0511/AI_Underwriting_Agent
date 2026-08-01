class RiskEngine:

    def calculate(
        self,
        probability
    ):

        risk_score = int(
            (1 - probability) * 1000
        )

        confidence = max(
            probability,
            1 - probability
        )

        confidence = round(
            confidence * 100,
            2
        )

        if probability < 0.10:

            bucket = "Very Low"

            recommendation = "Approve"

        elif probability < 0.20:

            bucket = "Low"

            recommendation = "Approve"

        elif probability < 0.35:

            bucket = "Medium"

            recommendation = "Manual Review"

        elif probability < 0.50:

            bucket = "High"

            recommendation = "Senior Underwriter Review"

        else:

            bucket = "Very High"

            recommendation = "Decline"

        return {

            "risk_score": risk_score,

            "probability_default": probability,

            "risk_bucket": bucket,

            "confidence": confidence,

            "recommendation": recommendation

        }