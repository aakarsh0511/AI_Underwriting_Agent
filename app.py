import streamlit as st

from src.data.data_loader import DataLoader

st.set_page_config(
    page_title="AI Underwriting Agent",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 AI Underwriting Agent")

st.markdown("---")

st.header("Offline Training Pipeline")

dataset_path = "data/raw/lending_club.csv"

try:

    loader = DataLoader(dataset_path)

    df = loader.load_data()

    summary = loader.dataset_summary(df)

    st.success("Dataset Loaded Successfully")

    st.subheader("Dataset Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rows", summary["Rows"])
    col2.metric("Columns", summary["Columns"])
    col3.metric("Missing Values", summary["Missing Values"])
    col4.metric("Duplicate Rows", summary["Duplicate Rows"])

    st.markdown("---")

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

except Exception as e:

    st.error(e)





import streamlit as st

from src.data.data_loader import DataLoader
from src.data.profiler import DataProfiler

st.set_page_config(
    page_title="AI Underwriting Agent",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 AI Underwriting Agent")

dataset_path = "data/raw/lending_club.csv"

loader = DataLoader(dataset_path)

df = loader.load_data()

summary = loader.dataset_summary(df)

st.success("Dataset Loaded Successfully")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Rows", summary["Rows"])
col2.metric("Columns", summary["Columns"])
col3.metric("Missing", summary["Missing Values"])
col4.metric("Duplicates", summary["Duplicate Rows"])

st.divider()

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Preview",
    "Missing Values",
    "Data Types",
    "Target",
    "High Cardinality",
    "Constant Columns"
])

with tab1:

    st.dataframe(df.head())

with tab2:

    st.dataframe(
        DataProfiler.missing_values(df)
    )

with tab3:

    st.dataframe(
        DataProfiler.data_types(df)
    )

with tab4:

    st.dataframe(
        DataProfiler.target_distribution(
            df,
            "loan_status"
        )
    )

with tab5:

    st.dataframe(
        DataProfiler.high_cardinality(df)
    )

with tab6:

    constant = DataProfiler.constant_columns(df)

    st.write(
        f"Total Constant Columns : {len(constant)}"
    )

    st.write(constant)