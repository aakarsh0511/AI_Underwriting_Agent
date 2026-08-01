import streamlit as st
from src.pipeline.training_pipeline import TrainingPipeline
from src.data.profiler import DataProfiler
from src.pipeline.prediction_pipeline import PredictionPipeline
from src.forms.application_form import CustomerApplicationForm
from src.pipeline.prediction_pipeline import PredictionPipeline
from src.risk.risk_engine import RiskEngine
from src.explainability.business_explainer import BusinessExplainer
from src.optimization.loan_optimizer import LoanOptimizer


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
    X_train = result["X_train"]
    X_test = result["X_test"]
    y_train = result["y_train"]
    y_test = result["y_test"]
    X_train_processed = result["X_train_processed"]
    X_test_processed = result["X_test_processed"]
    model_results = result["model_results"]
    best_model = result["best_model"]
    best_auc = result["best_auc"]
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
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13 = st.tabs([
    "Preview",
    "Missing Values",
    "Data Types",
    "Target Distribution",
    "High Cardinality",
    "Constant Columns",
    "Cleaning Summary",
    "Business Features",
    "Final Dataset",
    "Preprocessing",
    "Train/Test Split",
    "Model Training",
    "Prediction Test"
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

    st.subheader("Preprocessing")

    col1, col2 = st.columns(2)

    col1.metric(
        "Train Samples",
        X_train_processed.shape[0]
    )

    col2.metric(
        "Processed Features",
        X_train_processed.shape[1]
    )

    st.success("Preprocessing Completed")


with tab11:

    st.subheader("Train Test Split")

    col1, col2 = st.columns(2)

    col1.metric(
        "Training Samples",
        X_train.shape[0]
    )

    col2.metric(
        "Testing Samples",
        X_test.shape[0]
    )

    st.write("### Training Target Distribution")

    st.dataframe(
        y_train.value_counts()
        .rename_axis("Target")
        .reset_index(name="Count")
    )

    st.write("### Testing Target Distribution")

    st.dataframe(
        y_test.value_counts()
        .rename_axis("Target")
        .reset_index(name="Count")
    )
with tab12:

    st.subheader("Model Training")

    st.success(
        f"Best Model : {best_model}"
    )

    st.metric(
        "Best ROC AUC",
        best_auc
    )

    st.write("### Model Comparison")

    st.dataframe(
        model_results,
        use_container_width=True
    )

with tab13:

    form = CustomerApplicationForm()

    application = form.render()

    if application is not None:

        predictor = PredictionPipeline()

        prediction, probability = predictor.predict(
            application
        )

        risk_engine = RiskEngine()

        risk = risk_engine.calculate(
            probability
        )
        explainer = BusinessExplainer()
        explanation = explainer.explain(
            application)
        optimizer = LoanOptimizer()
        suggestions = optimizer.optimize(
            application)
        st.divider()
        st.subheader("Risk Intelligence")
        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)
        col1.metric(
            "Risk Score",
            risk["risk_score"]
        )
        col2.metric(
            "Probability of Default",
            f"{risk['probability_default']:.2%}"
        )
        col3.metric(
            "Risk Bucket",
            risk["risk_bucket"]
        )

        col4.metric(
            "Confidence",
            f"{risk['confidence']:.1f}%"
        )

        if risk["recommendation"] == "Approve":

            st.success(
                f"Recommendation: {risk['recommendation']}"
            )

        elif risk["recommendation"] == "Manual Review":

            st.warning(
                f"Recommendation: {risk['recommendation']}"
            )

        elif risk["recommendation"] == "Senior Underwriter Review":

            st.warning(
                f"Recommendation: {risk['recommendation']}"
            )

        else:

            st.error(
                f"Recommendation: {risk['recommendation']}"
            )
        st.divider()
        st.subheader("Business Explainability")
        col1, col2 = st.columns(2)
        with col1:
            st.success("Positive Factors")
            for item in explanation["positives"]:
                st.write(f"✅ {item}")
        with col2:

            st.error("Risk Factors")

            for item in explanation["negatives"]:

                st.write(f"❌ {item}")

        st.divider()
        st.subheader("Loan Optimization Suggestions")
        if len(suggestions) == 0:
            st.success(
                "No optimization required. The application already looks financially strong."
            )
        else:
            for i, suggestion in enumerate(suggestions, start=1):
                with st.expander(
                    f"Suggestion {i} - {suggestion['Category']}",
                    expanded=True
                ):
                    col1, col2 = st.columns(2)
                    col1.metric(
                        "Current",
                        suggestion["Current"]
                    )
                    col2.metric(
                        "Suggested",
                        suggestion["Suggested"]
                    )
                    st.info(
                        suggestion["Benefit"]
                    )