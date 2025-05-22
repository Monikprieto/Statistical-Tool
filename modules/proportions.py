import streamlit as st
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest
from scipy.stats import fisher_exact


def run_proportion_test(df):
    st.title("📊 Proportion Test (1 or 2 samples)")
    st.write("This module tests hypotheses about population proportions using Z-tests or Fisher's Exact Test.")

    test_type = st.radio("Select test type:", ["One Proportion", "Two Proportions", "Fisher Exact Test"])

    binary_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    if not binary_cols:
        st.warning("⚠️ No numeric columns found.")
        return

    if test_type == "One Proportion":
        st.subheader("🔍 One-Sample Proportion Test")
        alpha = st.slider("Select significance level (α)", 0.01, 0.10, 0.05)
        col = st.selectbox("Select binary outcome column (1 = success, 0 = failure):", binary_cols)
        prop_null = st.number_input("Enter null hypothesis proportion (e.g., 0.5)", min_value=0.0, max_value=1.0, value=0.5)

        if st.button("Run 1-Proportion Test"):
            sample = df[col].dropna()
            count = sample.sum()
            nobs = len(sample)
            z_stat, p_value = proportions_ztest(count, nobs, prop_null)

            st.success("Test Results")
            st.markdown(f"- ✅ **Z-statistic**: `{z_stat:.4f}`")
            st.markdown(f"- 📊 **P-value**: `{p_value:.4f}`")

            if p_value < alpha:
                st.warning("Reject the null hypothesis: The proportion is significantly different.")
            else:
                st.info("Fail to reject the null hypothesis: No significant difference found.")

    elif test_type == "Two Proportions":
        st.subheader("🔍 Two-Sample Proportion Test")
        alpha = st.slider("Select significance level (α)", 0.01, 0.10, 0.05)
        outcome_col = st.selectbox("Select binary outcome column (1 = success, 0 = failure):", binary_cols)
        group_col = st.selectbox("Select grouping column (should have exactly 2 categories):", df.columns)

        if st.button("Run 2-Proportion Test"):
            try:
                data = df[[group_col, outcome_col]].dropna()
                groups = data[group_col].unique()

                if len(groups) != 2:
                    st.error("Grouping column must have exactly two categories.")
                    return

                counts = data.groupby(group_col)[outcome_col].sum().values
                nobs = data.groupby(group_col)[outcome_col].count().values

                z_stat, p_value = proportions_ztest(counts, nobs)

                st.success("Test Results")
                st.markdown(f"- ✅ **Z-statistic**: `{z_stat:.4f}`")
                st.markdown(f"- 📊 **P-value**: `{p_value:.4f}`")

                if p_value < alpha:
                    st.warning("Reject the null hypothesis: The proportions are significantly different.")
                else:
                    st.info("Fail to reject the null hypothesis: No significant difference found.")
            except Exception as e:
                st.error(f"Error: {e}")

    elif test_type == "Fisher Exact Test":
        st.subheader("🔍 Fisher's Exact Test (2x2 Contingency Table)")
        alpha = st.slider("Select significance level (α)", 0.01, 0.10, 0.05)
        outcome_col = st.selectbox("Select binary outcome column (1 = success, 0 = failure):", binary_cols)
        group_col = st.selectbox("Select grouping column (must have 2 categories):", df.columns)

        if st.button("Run Fisher Exact Test"):
            try:
                data = df[[group_col, outcome_col]].dropna()
                groups = data[group_col].unique()

                if len(groups) != 2:
                    st.error("Grouping column must have exactly two categories.")
                    return

                contingency = pd.crosstab(data[group_col], data[outcome_col])
                if contingency.shape != (2, 2):
                    st.error("Contingency table must be 2x2.")
                    return

                odds_ratio, p_value = fisher_exact(contingency)

                st.success("Test Results")
                st.markdown(f"- 🧮 **Odds Ratio**: `{odds_ratio:.4f}`")
                st.markdown(f"- 📊 **P-value**: `{p_value:.4f}`")

                if p_value < alpha:
                    st.warning("Reject the null hypothesis: Variables are associated.")
                else:
                    st.info("Fail to reject the null hypothesis: No significant association found.")
            except Exception as e:
                st.error(f"Error: {e}")
