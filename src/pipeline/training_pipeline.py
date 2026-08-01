import pandas as pd
from src.data.data_loader import DataLoader
from src.data.data_cleaner import DataCleaner
from src.data.feature_engineering import FeatureEngineer
from src.data.feature_selector import FeatureSelector
from src.preprocessing.preprocessor import DataPreprocessor
from src.data.target_builder import TargetBuilder
class TrainingPipeline:
    def __init__(self):
        self.dataset_path = "data/raw/lending_club.csv"
    def run(self):
        loader = DataLoader(self.dataset_path)
        df = loader.load_data()
        cleaner = DataCleaner()
        df = cleaner.remove_duplicate_rows(df)

        df, constant_columns = cleaner.remove_constant_columns(df)

        df, dropped_columns = cleaner.remove_high_missing_columns(df)

        df = cleaner.fill_missing_values(df)

        engineer = FeatureEngineer()

        engineered_df = engineer.transform(df)

        selector = FeatureSelector()

        selected_df = selector.transform(engineered_df)

        target_builder = TargetBuilder()

        final_df = target_builder.transform(selected_df)

        final_df.to_csv(
            "data/processed/final_training_dataset.csv",
            index=False
        )

        X = final_df.drop(columns=["loan_status"])

        y = final_df["loan_status"]

        preprocessor = DataPreprocessor()

        X_processed = preprocessor.fit_transform(X)

        preprocessor.save()

        return {
            "raw_df": df,
            "engineered_df": engineered_df,
            "final_df": final_df,
            "X_processed": X_processed,
            "target": y,
            "constant_columns": constant_columns,
            "dropped_columns": dropped_columns
        }