import joblib


class PredictionPipeline:

    def __init__(self):

        self.model = joblib.load(
            "models/best_model.pkl"
        )

        self.preprocessor = joblib.load(
            "models/preprocessor.pkl"
        )

    def predict(self, application):

        processed = self.preprocessor.transform(
            application
        )

        probability = self.model.predict_proba(
            processed
        )[0][1]

        prediction = self.model.predict(
            processed
        )[0]

        return prediction, probability