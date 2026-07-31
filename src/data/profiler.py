import pandas as pd


class DataProfiler:

    @staticmethod
    def missing_values(df):
        missing = (
            df.isnull()
            .sum()
            .reset_index()
        )

        missing.columns = ["Column", "Missing Values"]

        missing["Percentage"] = (
            missing["Missing Values"] / len(df)
        ) * 100

        return missing.sort_values(
            by="Missing Values",
            ascending=False
        )

    @staticmethod
    def data_types(df):

        return pd.DataFrame({
            "Column": df.columns,
            "Data Type": df.dtypes.astype(str)
        })

    @staticmethod
    def target_distribution(df, target):

        return (
            df[target]
            .value_counts(dropna=False)
            .reset_index()
            .rename(
                columns={
                    "index": target,
                    target: "Count"
                }
            )
        )

    @staticmethod
    def constant_columns(df):

        cols = []

        for col in df.columns:

            if df[col].nunique(dropna=False) == 1:
                cols.append(col)

        return cols

    @staticmethod
    def high_cardinality(df, threshold=100):

        cols = []

        for col in df.select_dtypes(include="object"):

            if df[col].nunique() > threshold:
                cols.append(
                    {
                        "Column": col,
                        "Unique Values": df[col].nunique()
                    }
                )

        return pd.DataFrame(cols)