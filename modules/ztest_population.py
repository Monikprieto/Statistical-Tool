import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def run_ztest(df):
    st.header("📘 Z-Test: Sample vs Population")

    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    if len(numeric_cols) >= 1:
        col = st.selectbox("🔢 Select numeric sample column:", numeric_cols, key="ztest1")
        population_mean = st.number_input("📏 Enter population mean:", value=0.0, step=0.1)
        population_std = st.number_input("📐 Enter population standard deviation:", value=1.0, step=0.1)
        alpha = st.number_input("⚠️ Significance level (alpha):", value=0.05, step=0.01)

        if st.button("📊 Run Z-Test"):
            sample_data = df[col].dropna()
            sample_mean = sample_data.mean()
            n = len(sample_data)
            z_stat = (sample_mean - population_mean) / (population_std / np.sqrt(n))
            p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
            z_crit = stats.norm.ppf(1 - alpha / 2)

            # Resultados
            st.subheader("📈 Results")
            st.write(f"**Sample Size (n):** {n}")
            st.write(f"**Sample Mean:** {sample_mean:.4f}")
            st.write(f"**Z-Score:** {z_stat:.4f}")
            st.write(f"**Critical Value Z (±):** ±{z_crit:.4f}")
            st.write(f"**P-value (two-tailed):** {p_value:.4f}")

            if abs(z_stat) > z_crit:
                st.success("✅ Do you reject H₀? Yes — Significant difference")
            else:
                st.info("ℹ️ Do you reject H₀? No — Fail to reject null hypothesis")

            # Visualización
            fig, ax = plt.subplots(figsize=(7, 4))
            sns.histplot(sample_data, kde=True, ax=ax, color='skyblue')
            ax.axvline(population_mean, color='red', linestyle='--', label='Population Mean')
            ax.axvline(sample_mean, color='green', linestyle='--', label='Sample Mean')
            ax.set_title("Sample Distribution with Population Mean", fontsize=12)
            ax.set_xlabel("Value", fontsize=10)
            ax.set_ylabel("Density", fontsize=10)
            ax.tick_params(axis='both', labelsize=10)
            ax.legend(fontsize=8)

            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.pyplot(fig)
                
    else:
        st.warning("⚠️ You need at least one numeric column for Z-Test.")
