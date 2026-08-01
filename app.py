import streamlit as st

from src.pipeline.training_pipeline import TrainingPipeline
from src.data.profiler import DataProfiler


# --------------------------------------------------
# Streamlit Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Underwriting Agent",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 AI Underwriting Agent")
st.markdown("## Offline Training Pipeline")


# --------------------------------------------------
# Run Training Pipeline
# --------------------------------------------------

try:

    pipeline = TrainingPipeline()

    result = pipeline.run()

    df = result["raw_df"]
    engineered_df = result["engineered_df"]
    final_df = result["final_df"]
    X_processed = result["X_processed"]
    y = result["target"]

    constant_columns = result["constant_columns"]
    dropped_missing = result["dropped_columns"]

except Exception as e:

    st.error(e)
    st.stop()


# --------------------------------------------------
# Dataset Summary
# --------------------------------------------------

summary = {
    "Rows": df.shape[0],
    "Columns": df.shape[1],
    "Missing Values": int(df.isnull().sum().sum()),
    "Duplicate Rows": int(df.duplicated().sum())
}

col1, col2, col3, col4 = st.columns(4)

col1.metric("Rows", summary["Rows"])
col2.metric("Columns", summary["Columns"])
col3.metric("Missing Values", summary["Missing Values"])
col4.metric("Duplicate Rows", summary["Duplicate Rows"])

st.divider()


# --------------------------------------------------
# Tabs
# --------------------------------------------------

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs([
    "Preview",
    "Missing Values",
    "Data Types",
    "Target Distribution",
    "High Cardinality",
    "Constant Columns",
    "Cleaning Summary",
    "Business Features",
    "Final Training Dataset",
    "Preprocessing"
])


# --------------------------------------------------
# Preview
# --------------------------------------------------

with tab1:

    st.subheader("Dataset Preview")

    st.dataframe(df.head())


# --------------------------------------------------
# Missing Values
# --------------------------------------------------

with tab2:

    st.subheader("Missing Values")

    st.dataframe(
        DataProfiler.missing_values(df)
    )


# --------------------------------------------------
# Data Types
# --------------------------------------------------

with tab3:

    st.subheader("Data Types")

    st.dataframe(
        DataProfiler.data_types(df)
    )


# --------------------------------------------------
# Target Distribution
# --------------------------------------------------

with tab4:

    st.subheader("Target Distribution")

    st.dataframe(
        DataProfiler.target_distribution(
            final_df,
            "loan_status"
        )
    )


# --------------------------------------------------
# High Cardinality
# --------------------------------------------------

with tab5:

    st.subheader("High Cardinality Columns")

    st.dataframe(
        DataProfiler.high_cardinality(df)
    )


# --------------------------------------------------
# Constant Columns
# --------------------------------------------------

with tab6:

    st.subheader("Constant Columns")

    st.write(
        f"Total Constant Columns Removed : {len(constant_columns)}"
    )

    if len(constant_columns):

        st.write(constant_columns)

    else:

        st.success("No Constant Columns Found")


# --------------------------------------------------
# Cleaning Summary
# --------------------------------------------------

with tab7:

    st.subheader("Cleaning Summary")

    col1, col2 = st.columns(2)

    col1.metric(
        "Constant Columns Removed",
        len(constant_columns)
    )

    col2.metric(
        "High Missing Columns Removed",
        len(dropped_missing)
    )

    st.write("Final Shape After Cleaning")

    st.write(df.shape)


# --------------------------------------------------
# Business Features
# --------------------------------------------------

with tab8:

    st.subheader("Business Engineered Features")

    engineered_columns = [

        "monthly_income",
        "loan_to_income_ratio",
        "installment_income_ratio",
        "credit_history_years",
        "total_credit_exposure"

    ]

    available = [

        col
        for col in engineered_columns
        if col in engineered_df.columns

    ]

    st.write(
        f"Business Features Created : {len(available)}"
    )

    st.dataframe(
        engineered_df[available].head()
    )


# --------------------------------------------------
# Final Training Dataset
# --------------------------------------------------

with tab9:

    st.subheader("Final Training Dataset")

    col1, col2 = st.columns(2)

    col1.metric(
        "Rows",
        final_df.shape[0]
    )

    col2.metric(
        "Features",
        final_df.shape[1] - 1
    )

    st.write("### Target Distribution")

    st.dataframe(
        final_df["loan_status"]
        .value_counts()
        .rename_axis("Target")
        .reset_index(name="Count")
    )

    st.write(
        """
        Target Encoding

        0 → Fully Paid (Good Loan)

        1 → Charged Off (Bad Loan)
        """
    )

    st.dataframe(final_df.head())


# --------------------------------------------------
# Preprocessing
# --------------------------------------------------

with tab10:

    st.subheader("Preprocessing Summary")

    st.write(
        f"Processed Samples : {X_processed.shape[0]}"
    )

    st.write(
        f"Processed Features : {X_processed.shape[1]}"
    )

    st.success(
        "Preprocessor saved successfully."
    )