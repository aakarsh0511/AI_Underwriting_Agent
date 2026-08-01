import joblib
import pandas as pd
from src.data.feature_engineering import FeatureEngineer
class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(
            "models/best_model.pkl"
        )
        self.preprocessor = joblib.load(
            "models/preprocessor.pkl"
        )
        self.engineer = FeatureEngineer()
    def predict(self, input_df):
        engineered_df = self.engineer.transform(
            input_df
        )
        processed = self.preprocessor.transform(
            engineered_df
        )
        probability = self.model.predict_proba(
            processed
        )[0][1]
        prediction = self.model.predict(
            processed
        )[0]
        return prediction, probability