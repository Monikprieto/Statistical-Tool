import streamlit as st
import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

def run_logistic_regression(df):
    st.header("📗 Logistic Regression")

    if df is not None:
        st.subheader("📄 Preview of Uploaded Dataset")
        
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

        if len(numeric_cols) >= 2:
            y_col = st.selectbox("🎯 Select dependent (binary) variable (Y):", numeric_cols, key="logreg_y")
            x_cols = st.multiselect("🔢 Select one or more independent variable(s) (X):",
                                    [col for col in numeric_cols if col != y_col], key="logreg_x_multi")

            if x_cols and y_col:
                data = df[x_cols + [y_col]].dropna()
                X = data[x_cols]
                y = data[y_col]

                if y.nunique() == 2:
                    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                    scaler = StandardScaler()
                    X_train_scaled = scaler.fit_transform(X_train)
                    X_test_scaled = scaler.transform(X_test)

                    model = LogisticRegression()
                    model.fit(X_train_scaled, y_train)
                    y_pred = model.predict(X_test_scaled)

                    st.subheader("📊 Model Performance")
                    acc = accuracy_score(y_test, y_pred)
                    st.write(f"**Accuracy:** {acc:.4f}")
                    st.subheader("📈 Model Coefficients")
                    st.write("**Intercept (β₀):**", model.intercept_[0])
                    for feature, coef in zip(x_cols, model.coef_[0]):
                        st.write(f"**{feature} (β):** {coef:.4f}")
                    
                    st.subheader("📋 Confusion Matrix")
                    cm = confusion_matrix(y_test, y_pred)
                    fig, ax = plt.subplots(figsize=(15, 4), dpi=100)
                    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax, cbar=False, annot_kws={"size": 10})
                    ax.set_xlabel("Predicted", fontsize=9)
                    ax.set_ylabel("Actual", fontsize=9)
                    ax.set_title("Confusion Matrix", fontsize=12)
                    ax.tick_params(axis='both', labelsize=9)
                    st.pyplot(fig)
                else:
                    st.error("❌ Dependent variable must be binary (contain only two distinct values).")
                    
                        
        
        else:
            st.warning("⚠️ Please upload a dataset with at least two numeric columns.")
