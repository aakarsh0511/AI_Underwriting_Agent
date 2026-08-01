import pandas as pd
from src.data.data_loader import DataLoader
from src.data.data_cleaner import DataCleaner
from src.data.feature_engineering import FeatureEngineer
from src.data.feature_selector import FeatureSelector
from src.preprocessing.preprocessor import DataPreprocessor
from src.data.target_builder import TargetBuilder
from src.models.trainer import ModelTrainer
from src.data.dataset_splitter import DatasetSplitter
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
        splitter = DatasetSplitter()
        (
            X_train,
            X_test,
            y_train,
            y_test
        ) = splitter.split(X, y)
        preprocessor = DataPreprocessor()
        X_train_processed = preprocessor.fit_transform(
            X_train
        )
        X_test_processed = preprocessor.transform(
            X_test
        )
        preprocessor.save()
        trainer = ModelTrainer()
        training_result = trainer.train(
            X_train_processed,
            y_train,
            X_test_processed,
            y_test
        )

        return {
            "raw_df": df,
            "engineered_df": engineered_df,
            "final_df": final_df,
            "X_train": X_train,
            "X_test": X_test,
            "y_train": y_train,
            "y_test": y_test,
            "X_train_processed": X_train_processed,
            "X_test_processed": X_test_processed,
            "constant_columns": constant_columns,
            "dropped_columns": dropped_columns,
            "model_results": training_result["results"],
            "best_model": training_result["best_model"],
            "best_auc": training_result["best_auc"]
        }