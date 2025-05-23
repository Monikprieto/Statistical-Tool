import streamlit as st
import pandas as pd
from modules import proportions
from modules import descriptive, sampling, hypothesis, chi_square
from modules.correlation import correlation_selector
import base64
import numpy as np
import streamlit.components.v1 as components 
from statistical_resources import show_resources
from modules import linear_regression
from modules import logistic_regression
from modules import outliers_analysis
from modules import encoding_categorical


def render_html_table(df):
    table_html = df.to_html(classes="custom-table", index=False, escape=False)
    st.markdown(
        f"""
        <style>
        .custom-table {{
            border-collapse: collapse;
            width: 100%;
            font-family: 'Roboto', sans-serif;
        }}
        .custom-table th {{
            background-color: #004080;
            color: white;
            text-align: left;
            padding: 8px;
            border: 1px solid #cccccc;
        }}
        .custom-table td {{
            background-color: #ffffff;
            color: #000000;
            padding: 8px;
            border: 1px solid #dddddd;
        }}
        .custom-table tr:nth-child(even) {{
            background-color: #f2f2f2;
        }}
        </style>
        {table_html}
        """,
        unsafe_allow_html=True
    )
st.set_page_config(page_title="Statistica Tool", layout="wide")
st.title("📊 Statistica Tool")

st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# Load custom CSS
def load_custom_style():
    try:
        with open("assets/css/style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
            st.markdown("✅ CSS loaded!")
    except Exception as e:
        st.error(f"❌ Failed to load CSS: {e}")

load_custom_style()

import statistical_tables  
from analysis_guide import show_analysis_guide

st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to:", ["Analysis", "Statistical Tables Reference", "Analysis Guide", "Resources"])

if menu == "Analysis":
    st.sidebar.markdown("---")
    module = st.sidebar.selectbox("📚 Select Analysis Module", [
        "Descriptive Analysis", "Sampling", "Categorical Encoding",
        "Hypothesis Testing", "Tests whitout BD","Correlation", "Chi-Square Test", "Proportion Test",
        "Linear Regression", "Logistic Regression", "Outliers"], key="module_select")

if menu == "Statistical Tables Reference":
    statistical_tables.main()
elif menu == "Analysis Guide":
    show_analysis_guide()
elif menu == "Resources":
    show_resources()

st.sidebar.markdown("---")

uploaded_file = st.sidebar.file_uploader("📁 Upload a CSV file", type="csv")
df = None
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        uploaded_file.seek(0)
        st.session_state["uploaded_file"] = pd.read_csv(uploaded_file)
        st.sidebar.success("✅ File uploaded successfully!")
    except Exception as e:
        st.sidebar.error(f"❌ File upload error: {e}")
        st.session_state["uploaded_file"] = None

st.sidebar.markdown("---")

def download_link(file_path, filename, link_text):
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{link_text}</a>'
    return href

st.sidebar.markdown("📄 Need a sample file download?")
st.sidebar.markdown(download_link("chi_square_template.csv", "chi_square_template.csv", "🔽Chi-Square Template"), unsafe_allow_html=True)
st.sidebar.markdown(download_link("sampling_template.csv", "sampling_template.csv", "🔽Sampling Template"), unsafe_allow_html=True)
st.sidebar.markdown(download_link("descriptive_template.csv", "descriptive_template.csv", "🔽Descriptive Template"), unsafe_allow_html=True)
st.sidebar.markdown(download_link("ztest_template.csv", "ztest_template.csv", "🔽Z-Test Template"), unsafe_allow_html=True)
st.sidebar.markdown(download_link("ttest_template.csv", "ttest_template.csv", "🔽T-Test Template"), unsafe_allow_html=True)
st.sidebar.markdown(download_link("one_way_anova_template.csv", "one_way_anova_template.csv", "🔽One-Way ANOVA Template"), unsafe_allow_html=True)
st.sidebar.markdown(download_link("two_way_anova_template.csv", "two_way_anova_template.csv", "🔽Two-Way ANOVA Template"), unsafe_allow_html=True)
st.sidebar.markdown(download_link("tukey_template.csv", "tukey_template.csv", "🔽Tukey Test Template"), unsafe_allow_html=True)
st.sidebar.markdown(download_link("correlation_template.csv", "correlation_template.csv", "🔽Correlation Template"), unsafe_allow_html=True)
st.sidebar.markdown(download_link("proportion_test_template.csv", "proportion_test_template.csv", "🔽Proportion Test Template"), unsafe_allow_html=True)
st.sidebar.markdown(download_link("two_proportions_template.csv", "two_proportions_template.csv", "🔽Two-Proportions Template"), unsafe_allow_html=True)
st.sidebar.markdown(download_link("fisher_exact_template.csv", "fisher_exact_template.csv", "🔽Fisher Exact Test Template"), unsafe_allow_html=True)
st.sidebar.markdown(download_link("linear_regression_template.csv", "linear_regression_template.csv", "🔽Linear Regression Template"), unsafe_allow_html=True)
st.sidebar.markdown(download_link("logistic_regression_template.csv", "logistic_regression_template.csv", "🔽Logistic Regression Template"), unsafe_allow_html=True)
st.sidebar.markdown(download_link("outliers_template.csv", "outliers_template.csv", "🔽Outliers Template"), unsafe_allow_html=True)
st.sidebar.markdown(download_link("encoding_template.csv", "encoding_template.csv", "🔽Encoding Template"), unsafe_allow_html=True)

df = st.session_state.get("uploaded_file")


if menu == "Analysis":
    if module == "Tests whitout BD":
        import modules.stat_tests_menu as stat_tests_menu
        stat_tests_menu.run()

    elif df is None:
        st.info("Please upload a CSV file to start analysis.")

    else:
        # ✅ Mostrar preview solo si hay archivo y no es "Tests whitout BD"
        st.subheader("📄 Preview of Uploaded Dataset")
        render_html_table(df.head())

        if module == "Descriptive Analysis":
            numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
            if numeric_cols:
                selected_col = st.selectbox("🔢 Select a numeric column to analyze:", numeric_cols, key="desc")
                if st.button("▶️ Run Descriptive Analysis"):
                    st.subheader(f"📈 Descriptive Statistics for '{selected_col}'")
                    descriptive.run_descriptive_analysis(df[selected_col].dropna(), selected_col)
            else:
                st.warning("⚠️ No numeric columns found in the dataset.")

        elif module == "Sampling":
            numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
            if numeric_cols:
                selected_col = st.selectbox("📌 Select a numeric column for sampling analysis:", numeric_cols, key="samp")
                confidence = st.number_input("🔒 Confidence Level (50-99.9%)", min_value=50.0, max_value=99.9, value=95.0)
                if st.button("📊 Run Sampling Analysis"):
                    st.subheader(f"📊 Sampling Statistics for '{selected_col}'")
                    sampling.run_sampling_analysis(df[selected_col].dropna(), confidence)
            else:
                st.warning("⚠️ No numeric columns found in the dataset.")

        elif module == "Categorical Encoding":
            encoding_categorical.run_encoding_tool(df)

        elif module == "Hypothesis Testing":
            hypothesis.hypothesis_test_menu(df)

        elif module == "Correlation":
            correlation_selector(df)

        elif module == "Chi-Square Test":
            chi_square.run_chi_square_test()

        elif module == "Proportion Test":
            proportions.run_proportion_test(df)

        elif module == "Linear Regression":
            linear_regression.run_linear_regression()

        elif module == "Logistic Regression":
            logistic_regression.run_logistic_regression(df)

        elif module == "Outliers":
            outliers_analysis.run_outlier_analysis(df)
