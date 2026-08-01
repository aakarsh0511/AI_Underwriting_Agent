import joblib

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer


class DataPreprocessor:

    def __init__(self):

        self.preprocessor = None

    def fit(self, X):

        categorical_columns = X.select_dtypes(
            include=["object"]
        ).columns.tolist()

        numerical_columns = X.select_dtypes(
            exclude=["object"]
        ).columns.tolist()

        numeric_pipeline = Pipeline(
            steps=[
                (
                    "imputer",
                    SimpleImputer(strategy="median")
                ),
                (
                    "scaler",
                    StandardScaler()
                )
            ]
        )

        categorical_pipeline = Pipeline(
            steps=[
                (
                    "imputer",
                    SimpleImputer(strategy="most_frequent")
                ),
                (
                    "encoder",
                    OneHotEncoder(
                        handle_unknown="ignore"
                    )
                )
            ]
        )

        self.preprocessor = ColumnTransformer(
            transformers=[
                (
                    "numeric",
                    numeric_pipeline,
                    numerical_columns
                ),
                (
                    "categorical",
                    categorical_pipeline,
                    categorical_columns
                )
            ]
        )

        self.preprocessor.fit(X)

        return self.preprocessor

    def transform(self, X):

        return self.preprocessor.transform(X)

    def fit_transform(self, X):

        self.fit(X)

        return self.transform(X)

    def save(self):

        joblib.dump(
            self.preprocessor,
            "models/preprocessor.pkl"
        )