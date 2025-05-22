import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.stats import pearsonr, spearmanr, kendalltau, pointbiserialr, chi2_contingency
import numpy as np

def run_correlation(df, col1, col2, method='Pearson'):
    st.write(f"### 📈 {method} Correlation Analysis")

    # Conversión a numérico
    x = pd.to_numeric(df[col1], errors='coerce')
    y = pd.to_numeric(df[col2], errors='coerce')

    # Eliminar valores NaN y alinear longitudes
    valid_idx = x.notna() & y.notna()
    x = x[valid_idx]
    y = y[valid_idx]

    if len(x) < 2 or len(y) < 2:
        st.error("❌ Not enough valid numeric data to compute correlation.")
        return

    alpha = 0.05

    if method == 'Pearson':
        r, p = pearsonr(x, y)
        st.write(f"**Pearson Correlation Coefficient (r):** {r:.4f}")
    elif method == 'Spearman':
        r, p = spearmanr(x, y)
        st.write(f"**Spearman Rank Correlation (ρ):** {r:.4f}")
    elif method == 'Kendall':
        r, p = kendalltau(x, y)
        st.write(f"**Kendall Tau Correlation (τ):** {r:.4f}")
    elif method == 'Point-Biserial':
        if len(x.unique()) == 2:
            r, p = pointbiserialr(x, y)
        else:
            r, p = pointbiserialr(y, x)
        st.write(f"**Point-Biserial Correlation (rpb):** {r:.4f}")
    elif method == 'Chi-Square (Phi)':
        x_cat = df[col1].astype(str)
        y_cat = df[col2].astype(str)
        contingency_table = pd.crosstab(x_cat, y_cat)
        chi2, p, _, _ = chi2_contingency(contingency_table)
        phi = np.sqrt(chi2 / contingency_table.sum().sum())
        st.write(f"**Chi-Square Statistic (χ²):** {chi2:.4f}")
        st.write(f"**Phi Coefficient:** {phi:.4f}")
        r = phi  # Para coherencia visual con otras correlaciones
    else:
        st.error("Método de correlación no soportado.")
        return

    st.write(f"**P-value:** {p:.4f}")
    if p < alpha:
        st.success("✅ Result: Significant correlation (reject H₀)")
    else:
        st.info("ℹ️ Result: No significant correlation (fail to reject H₀)")

    if method in ['Pearson', 'Spearman', 'Kendall', 'Point-Biserial']:
        st.write("### 🔍 Scatter Plot with Regression Line")
        col1_plot, col2_plot = st.columns([2, 1])
        with col1_plot:
            fig, ax = plt.subplots(figsize=(4, 3))
            sns.regplot(x=x, y=y, ax=ax, line_kws={'color': 'red'})
            ax.set_title(f"{col1} vs {col2}", fontsize=8)
            ax.set_xlabel(col1, fontsize=6)
            ax.set_ylabel(col2, fontsize=6)
            ax.tick_params(axis='both', labelsize=5)
            col1_sp, col2_sp, col3_sp = st.columns([1, 2, 1])
            with col2_sp:
                st.pyplot(fig)

def show_correlation_matrix(df):
    st.write("### 🧮 Correlation Matrices")
    num_cols = df.select_dtypes(include=[np.number])

    for method in ['pearson', 'spearman', 'kendall']:
        st.write(f"#### {method.title()} Correlation Matrix")
        corr_matrix = num_cols.corr(method=method)
        st.dataframe(corr_matrix.style.background_gradient(cmap='coolwarm', axis=None))
        col1_plot, col2_plot = st.columns([2, 1])
        with col1_plot:
            fig, ax = plt.subplots(figsize=(4, 3))
            sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5,
                        cbar_kws={"shrink": 0.6})
            ax.set_title(f"{method.title()} Correlation Heatmap", fontsize=8)
            ax.tick_params(axis='both', labelsize=5)
            col1_m, col2_m, col3_m = st.columns([1, 2, 1])
            with col2_m:
                st.pyplot(fig)

def correlation_selector(df):
    st.subheader("Correlation Tool")
    num_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    bin_cols = df.select_dtypes(include=['int64', 'object', 'bool']).nunique()
    bin_cols = bin_cols[bin_cols == 2].index.tolist()
    all_cols = list(set(num_cols + bin_cols))

    if len(all_cols) < 2:
        st.warning("Need at least two usable columns.")
        return

    col1 = st.selectbox("Select X variable:", all_cols)
    col2 = st.selectbox("Select Y variable:", [col for col in all_cols if col != col1])
    method = st.selectbox("Correlation Method:", ["Pearson", "Spearman", "Kendall", "Point-Biserial", "Chi-Square (Phi)"])
    run_correlation(df, col1, col2, method)

    st.markdown("---")
    show_matrices = st.checkbox("🔍 Show Correlation Matrices")
    if show_matrices:
        show_correlation_matrix(df)
