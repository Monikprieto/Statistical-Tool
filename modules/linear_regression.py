import streamlit as st
import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns


def run_linear_regression():
    st.header("📘 Linear Regression")

    df = st.session_state.get("uploaded_file")
    if df is not None:
        st.subheader("📄 Preview of Uploaded Dataset")
        st.dataframe(df.head())

        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

        if len(numeric_cols) >= 2:
            dep_var = st.selectbox("📌 Select the dependent variable:", numeric_cols)
            indep_vars = st.multiselect("🛠️ Select one or more independent variables:",
                                        [col for col in numeric_cols if col != dep_var])

            if dep_var and indep_vars:
                X = df[indep_vars]
                y = df[dep_var]

                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                X_train_const = sm.add_constant(X_train)
                model = sm.OLS(y_train, X_train_const).fit()

                X_test_const = sm.add_constant(X_test)
                y_pred = model.predict(X_test_const)

                st.subheader("📊 Model Summary")
                summary_df = model.summary2().tables[0].copy()
                styled_summary = summary_df.style.set_properties(**{
                    'background-color': '#ffffff',
                    'color': '#0d2b45',
                    'border-color': '#4d82bc',
                    'font-family': 'Roboto',
                    'font-size': '14px',
                    'width': '200px'
                })
                st.write(styled_summary)

                st.subheader("📈 Coefficients Table")
                coef_df = model.summary2().tables[1]
                styled_coef = coef_df.style.set_properties(**{
                    'background-color': '#ffffff',
                    'color': '#0d2b45',
                    'border-color': '#4d82bc',
                    'font-family': 'Roboto',
                    'font-size': '14px'
                })
                st.write(styled_coef)

                st.subheader("📉 Residual Plot")
                residuals = y_test - y_pred
                fig, ax = plt.subplots(figsize=(15, 4))
                sns.residplot(x=y_pred, y=residuals, ax=ax, color="#4d82bc", lowess=True)
                ax.set_title("Residual Plot", fontsize=12)
                ax.set_xlabel("Predicted Values", fontsize=10)
                ax.set_ylabel("Residuals", fontsize=10)
                ax.tick_params(labelsize=10)
                st.pyplot(fig)

                st.success("✅ Linear regression analysis completed successfully.")
        else:
            st.warning("⚠️ Please upload a dataset with at least two numeric columns.")
