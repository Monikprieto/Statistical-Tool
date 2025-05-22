import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

def run_outlier_analysis(df):
    st.header("📘 Outlier Detection")

    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    if not numeric_cols:
        st.warning("⚠️ You need at least one numeric column.")
        return

    selected_col = st.selectbox("🔢 Select column to analyze:", numeric_cols)
    method = st.radio("🛠️ Select detection method:", ["Z-Score", "IQR"])

    data = df[selected_col].dropna()

    if method == "Z-Score":
        threshold = st.slider("Set Z-Score threshold", 1.5, 4.0, 3.0, 0.1)
        z_scores = np.abs(stats.zscore(data))
        outliers = data[z_scores > threshold]
    else:
        q1 = data.quantile(0.25)
        q3 = data.quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        outliers = data[(data < lower) | (data > upper)]

    st.subheader("🔍 Outlier Summary")
    st.write(f"**Total values analyzed:** {len(data)}")
    st.write(f"**Outliers detected:** {len(outliers)}")

    if not outliers.empty:
        st.dataframe(outliers.to_frame(name=selected_col).reset_index(drop=True))

    st.subheader("📊 Visualization")

    # Boxplot
    fig1, ax1 = plt.subplots(figsize=(3, 1.5))
    sns.boxplot(x=data, ax=ax1, color='lightblue')
    ax1.set_title("Boxplot", fontsize=8)
    ax1.set_xlabel(selected_col, fontsize=6)
    ax1.tick_params(labelsize=5)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.pyplot(fig1)

    # Histogram
    fig2, ax2 = plt.subplots(figsize=(3, 2))
    sns.histplot(data, kde=True, ax=ax2, color='skyblue')
    ax2.set_title("Distribution with Outliers", fontsize=8)
    ax2.set_xlabel(selected_col, fontsize=6)
    ax2.set_ylabel("Frequency", fontsize=6)
    ax2.tick_params(labelsize=5)
    for val in outliers:
        ax2.axvline(val, color='red', linestyle='--', linewidth=0.5)
    col1h, col2h, col3h = st.columns([1, 2, 1])
    with col2h:
        st.pyplot(fig2)
