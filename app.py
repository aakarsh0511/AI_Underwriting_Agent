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