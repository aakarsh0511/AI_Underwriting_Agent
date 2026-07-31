import streamlit as st

st.set_page_config(
    page_title="AI Underwriting Agent",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 AI Underwriting Agent")

st.markdown("---")

st.header("Welcome")

st.write(
    """
    This application assists loan underwriters in making
    explainable, policy-compliant, AI-powered lending decisions.
    """
)

st.success("Project setup completed successfully.")