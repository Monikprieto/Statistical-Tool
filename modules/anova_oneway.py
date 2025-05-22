import streamlit as st
import numpy as np
import pandas as pd
from scipy.stats import f
import matplotlib.pyplot as plt
import seaborn as sns

def run_anova_oneway(df, group_col, value_col):
    st.header("📘 One-Way ANOVA")

    try:
        groups = df[group_col].unique()
        group_data = [
            df[df[group_col] == g][value_col].dropna()
            for g in groups
        ]
        all_data = pd.concat(group_data)

        k = len(groups)
        n = len(all_data)
        grand_mean = np.mean(all_data)

        ssb = sum(len(g) * (np.mean(g) - grand_mean) ** 2 for g in group_data)
        ssw = sum(sum((x - np.mean(g)) ** 2 for x in g) for g in group_data)
        sst = ssb + ssw

        msb = ssb / (k - 1)
        msw = ssw / (n - k)
        mst = sst / (n - 1)
        f_stat = msb / msw

        alpha = 0.05
        f_crit = f.ppf(1 - alpha, dfn=k - 1, dfd=n - k)
        p_value = 1 - f.cdf(f_stat, dfn=k - 1, dfd=n - k)

        # Mostrar resultados
        st.subheader("📋 ANOVA Summary")
        st.write(f"**Grand Mean:** {grand_mean:.4f}")
        st.write(f"**Total Sum of Squares (SST):** {sst:.4f}")
        st.write(f"**Mean Square Total (MST):** {mst:.4f}")
        st.write(f"**Sum of Squares Between (SSB):** {ssb:.4f}")
        st.write(f"**Mean Square Between (MSB):** {msb:.4f}")
        st.write(f"**Sum of Squares Within (SSW):** {ssw:.4f}")
        st.write(f"**Mean Square Within (MSW):** {msw:.4f}")
        st.write(f"**F-Statistic:** {f_stat:.4f}")
        st.write(f"**Critical Value of F (alpha=0.05):** {f_crit:.4f}")
        st.write(f"**P-Value:** {p_value:.4f}")

        if f_stat > f_crit:
            st.success("✅ Result: Reject the null hypothesis (significant difference)")
        else:
            st.info("ℹ️ Result: Fail to reject the null hypothesis")

        # Visualización
        st.subheader("📊 Visual Summary")
        fig, axs = plt.subplots(1, 2, figsize=(8, 3))

        # Boxplot
        sns.boxplot(x=df[group_col], y=df[value_col], ax=axs[0], palette="pastel")
        axs[0].set_title("Boxplot by Group")
        axs[0].set_xlabel(group_col)
        axs[0].set_ylabel(value_col)

        # Medias ± error estándar
        means = df.groupby(group_col)[value_col].mean()
        sems = df.groupby(group_col)[value_col].sem()
        axs[1].bar(means.index, means.values, yerr=sems.values, capsize=10, color='lightblue')
        axs[1].set_title("Group Means ± SE")
        axs[1].set_xlabel(group_col)
        axs[1].set_ylabel("Mean")

        plt.tight_layout()
        st.pyplot(fig)

    except Exception as e:
        st.error(f"🚫 Error running One-Way ANOVA: {e}")
