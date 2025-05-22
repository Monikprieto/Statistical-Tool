import streamlit as st
from modules import ttest_two_groups, ztest_population, anova_oneway, anova_twoway, tukey_posthoc

def hypothesis_test_menu(df):
    st.title("📊 Hypothesis Testing")

    test_type = st.selectbox("Choose the hypothesis test:", [
        "T-Test (Two Groups)",
        "Z-Test (Sample vs Population)",
        "One-Way ANOVA",
        "Two-Way ANOVA",
        "Tukey Post-Hoc Test"
    ])

    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

    if test_type == "T-Test (Two Groups)":
        ttest_two_groups.run_ttest(df)

    elif test_type == "Z-Test (Sample vs Population)":
        ztest_population.run_ztest(df)

    elif test_type == "One-Way ANOVA":
        if len(categorical_cols) >= 1 and len(numeric_cols) >= 1:
            group_col = st.selectbox("🔠 Select categorical group column:", categorical_cols, key="anova1")
            value_col = st.selectbox("🔢 Select numeric value column:", numeric_cols, key="anova2")
            if st.button("📊 Run One-Way ANOVA"):
                anova_oneway.run_anova_oneway(df.dropna(subset=[group_col, value_col]), group_col, value_col)
        else:
            st.warning("⚠️ You need at least one categorical and one numeric column.")

    elif test_type == "Two-Way ANOVA":
        if len(categorical_cols) >= 2 and len(numeric_cols) >= 1:
            factor1 = st.selectbox("🔠 Select first categorical factor:", categorical_cols, key="factor1")
            factor2 = st.selectbox("🔠 Select second categorical factor:", categorical_cols, key="factor2")
            value_col = st.selectbox("🔢 Select numeric value column:", numeric_cols, key="value2")
            if st.button("📊 Run Two-Way ANOVA"):
                anova_twoway.run_anova_twoway(df.dropna(subset=[factor1, factor2, value_col]), factor1, factor2, value_col)
        else:
            st.warning("⚠️ You need at least two categorical and one numeric column.")

    elif test_type == "Tukey Post-Hoc Test":
        if len(categorical_cols) >= 1 and len(numeric_cols) >= 1:
            group_col = st.selectbox("🔠 Select categorical group column:", categorical_cols, key="tukey_group")
            value_col = st.selectbox("🔢 Select numeric value column:", numeric_cols, key="tukey_value")
            if st.button("📊 Run Tukey Test"):
                tukey_posthoc.run_tukey_test(df.dropna(subset=[group_col, value_col]), group_col, value_col)
        else:
            st.warning("⚠️ You need at least one categorical and one numeric column.")
