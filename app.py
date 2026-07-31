import streamlit as st

from src.data.data_loader import DataLoader
from src.data.data_cleaner import DataCleaner
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
df = loader.load_data()
cleaner = DataCleaner()
df = cleaner.remove_duplicate_rows(df)
df, constant_columns = cleaner.remove_constant_columns(df)
df, dropped_missing = cleaner.remove_high_missing_columns(df)
df = cleaner.fill_missing_values(df)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Rows", summary["Rows"])
col2.metric("Columns", summary["Columns"])
col3.metric("Missing", summary["Missing Values"])
col4.metric("Duplicates", summary["Duplicate Rows"])

st.divider()

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "Preview",
    "Missing Values",
    "Data Types",
    "Target",
    "High Cardinality",
    "Constant Columns",
    "Cleaning Summary"
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
with tab7:

    st.subheader("Cleaning Report")

    st.write(
        f"Constant Columns Removed : {len(constant_columns)}"
    )

    st.write(
        f"High Missing Columns Removed : {len(dropped_missing)}"
    )

    st.write("Remaining Dataset Shape")

    st.write(df.shape)

    st.write(constant)


