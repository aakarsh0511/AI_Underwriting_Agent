import pandas as pd


class DataLoader:
    """
    Handles loading the historical lending dataset.
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        """
        Load dataset from CSV.
        """

        df = pd.read_csv(
            self.file_path,
            low_memory=False
        )

        return df

    @staticmethod
    def dataset_summary(df):

        return {
            "Rows": df.shape[0],
            "Columns": df.shape[1],
            "Missing Values": int(df.isnull().sum().sum()),
            "Duplicate Rows": int(df.duplicated().sum())
        }