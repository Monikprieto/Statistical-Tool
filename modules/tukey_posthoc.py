import streamlit as st
import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt
import seaborn as sns

def run_tukey_test(data, group_col, value_col):
    st.header("📘 Tukey's Post-Hoc Test")

    try:
        tukey = pairwise_tukeyhsd(endog=data[value_col], groups=data[group_col], alpha=0.05)

        st.subheader("📋 Tukey HSD Summary")
        result_df = pd.DataFrame(data=tukey.summary().data[1:], columns=tukey.summary().data[0])
        st.dataframe(result_df)

        # Gráfico de comparaciones múltiples
        st.subheader("📈 Tukey HSD Plot")
        fig = tukey.plot_simultaneous(figsize=(4, 2))
        fig.suptitle("Tukey HSD Plot", fontsize=8)
        for ax in fig.axes:
            ax.tick_params(axis='both', labelsize=6)
            ax.set_title("")  # Borra el título superpuesto
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.pyplot(fig.figure)


        # Boxplot para visualización de grupos
        st.subheader("📊 Group Distribution (Boxplot)")
        fig2, ax = plt.subplots(figsize=(4, 2))
        sns.boxplot(x=group_col, y=value_col, data=data, ax=ax, palette="pastel")
        ax.set_title("Group Distribution", fontsize=8)
        ax.set_xlabel(group_col, fontsize=6)
        ax.set_ylabel(value_col, fontsize=6)
        ax.tick_params(axis='both', labelsize=5)
        plt.xticks(rotation=45)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.pyplot(fig2)

    except Exception as e:
        st.error(f"🚫 Error running Tukey test: {e}")
