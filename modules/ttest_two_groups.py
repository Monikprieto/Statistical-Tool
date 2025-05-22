import streamlit as st
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

def run_ttest(df):
    st.header("📘 T-Test: Two Independent Groups")
    
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    
    if len(numeric_cols) >= 2:
        col1 = st.selectbox("🧪 Select first group column:", numeric_cols, key="hyp1")
        col2 = st.selectbox("🧪 Select second group column:", numeric_cols, key="hyp2")
        equal_var = st.checkbox("Assume equal variances (Student's t-test)", value=True)
        
        if st.button("🔬 Run T-Test"):
            group1 = df[col1].dropna()
            group2 = df[col2].dropna()

            t_stat, p_value = stats.ttest_ind(group1, group2, equal_var=equal_var)

            st.subheader(f"T-Test between '{col1}' and '{col2}'")
            st.write(f"**Sample sizes:** {len(group1)} (Group 1), {len(group2)} (Group 2)")
            st.write(f"**T-statistic:** {t_stat:.4f}")
            st.write(f"**P-value:** {p_value:.4f}")
            st.write("**Do you reject H₀?** " + ("✅ Yes, reject the null hypothesis." if p_value < 0.05 else "❌ No, fail to reject the null hypothesis."))

            # Visual: Histogram of both groups
            fig, ax = plt.subplots(figsize=(7, 4))
            sns.histplot(group1, kde=True, color="blue", label=col1, ax=ax)
            sns.histplot(group2, kde=True, color="orange", label=col2, ax=ax)
            ax.set_title("Distribution of the Two Groups", fontsize=12)
            ax.set_xlabel(col1 + " / " + col2, fontsize=10)
            ax.set_ylabel("Count", fontsize=10)
            ax.tick_params(axis='both', labelsize=10)  # Tamaño de los números en los ejes
            ax.legend(fontsize=8)
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.pyplot(fig)

    else:
        st.warning("⚠️ At least two numeric columns are required for T-Test.")
