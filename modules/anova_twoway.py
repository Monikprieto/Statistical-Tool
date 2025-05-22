import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy.stats import f

def run_anova_twoway(df, factor1, factor2, value_col):
    st.header("📘 Two-Way ANOVA")

    try:
        st.subheader(f"Two-Way ANOVA: {value_col} by {factor1} and {factor2}")
        formula = f'{value_col} ~ C({factor1}) + C({factor2}) + C({factor1}):C({factor2})'
        model = ols(formula, data=df).fit()
        aov = sm.stats.anova_lm(model, typ=2)

        alpha = 0.05
        df_within = aov.iloc[-1]['df']
        summary_rows = []

        for effect in [f'C({factor1})', f'C({factor2})', f'C({factor1}):C({factor2})']:
            if effect in aov.index:
                row = aov.loc[effect]
                df_effect = row['df']
                ms = row['sum_sq'] / row['df']
                fval = row['F']
                pval = row['PR(>F)']
                fcrit = f.ppf(1 - alpha, dfn=df_effect, dfd=df_within)
                decision = "Reject H₀" if pval < alpha else "Fail to reject H₀"
                summary_rows.append([
                    effect, row['sum_sq'], df_effect, ms, fval, pval, fcrit, decision
                ])

        # Residual
        residual = aov.loc['Residual']
        ms_residual = residual['sum_sq'] / residual['df']
        summary_rows.append([
            'Residual', residual['sum_sq'], residual['df'], ms_residual, '', '', '', ''
        ])

        df_summary = pd.DataFrame(summary_rows, columns=[
            "Source of Variation", "SS", "df", "MS", "F", "P-value", "F crit", "Decision"
        ])
        st.subheader("📋 ANOVA Summary")
        st.dataframe(df_summary)

        # Visualización
        st.subheader("📊 Visual Summary")
        fig, axs = plt.subplots(1, 2, figsize=(8, 3))

        sns.boxplot(x=df[factor1], y=df[value_col], hue=df[factor2], ax=axs[0], palette="pastel")
        axs[0].legend(title=factor2, loc='upper right', fontsize='small')
        axs[0].set_title("Boxplot by Group")
        axs[0].set_xlabel(factor1)
        axs[0].set_ylabel(value_col)

        interaction_means = df.groupby([factor1, factor2])[value_col].mean().unstack()
        interaction_sems = df.groupby([factor1, factor2])[value_col].sem().unstack()
        interaction_means.plot(kind='bar', yerr=interaction_sems, ax=axs[1], capsize=4, colormap='Set2')
        axs[1].set_xticklabels(interaction_means.index, rotation=0)
        axs[1].set_title("Means ± SE by Group Interaction")
        axs[1].set_ylabel("Mean")
        axs[1].legend(title=factor2, loc='upper right', fontsize='small')

        plt.tight_layout()
        st.pyplot(fig)

    except Exception as e:
        st.error(f"🚫 Error running Two-Way ANOVA: {e}")
