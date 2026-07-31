import pandas as pd


class DataCleaner:

    def __init__(self, missing_threshold=70):
        self.missing_threshold = missing_threshold

    def remove_duplicate_rows(self, df):

        return df.drop_duplicates()

    def remove_constant_columns(self, df):

        constant_columns = [
            col for col in df.columns
            if df[col].nunique(dropna=False) <= 1
        ]

        return df.drop(columns=constant_columns), constant_columns

    def remove_high_missing_columns(self, df):

        percentage = (
            df.isnull().mean() * 100
        )

        columns_to_drop = percentage[
            percentage > self.missing_threshold
        ].index.tolist()

        return df.drop(columns=columns_to_drop), columns_to_drop

    def fill_missing_values(self, df):

        numeric_columns = df.select_dtypes(
            include=["number"]
        ).columns

        categorical_columns = df.select_dtypes(
            include=["object"]
        ).columns

        for col in numeric_columns:

            df[col] = df[col].fillna(
                df[col].median()
            )

        for col in categorical_columns:

            df[col] = df[col].fillna(
                df[col].mode()[0]
            )

        return df