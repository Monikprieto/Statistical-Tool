
import streamlit as st
from scipy.stats import t
import numpy as np

def run():
    st.header("📉 T-Test for Independent Samples (Equal Variances)")

    st.markdown("Use this test when population variances are assumed to be equal.")

    with st.form("t_test_equal_var_form"):
        st.subheader("Enter Sample Data")

        data1 = st.text_area("Sample 1 Data (comma-separated)", "94,86,120,105,99,110,104,112,115,93,117,114")
        data2 = st.text_area("Sample 2 Data (comma-separated)", "112,107,111,112,100,115,109,119,93,126")

        alpha = st.number_input("Significance Level (α)", min_value=0.01, max_value=0.10, step=0.01, value=0.05)

        alternative = st.selectbox(
            "Alternative Hypothesis (H₁)",
            ["μ₁ ≠ μ₂ (Two-tailed)", "μ₁ > μ₂ (Right-tailed)", "μ₁ < μ₂ (Left-tailed)"]
        )

        submitted = st.form_submit_button("Run T-Test")

    if submitted:
        try:
            x1 = np.array([float(i.strip()) for i in data1.split(",")])
            x2 = np.array([float(i.strip()) for i in data2.split(",")])

            n1, n2 = len(x1), len(x2)
            mean1, mean2 = np.mean(x1), np.mean(x2)
            var1, var2 = np.var(x1, ddof=1), np.var(x2, ddof=1)

            pooled_var = ((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2)
            pooled_se = np.sqrt(pooled_var * (1/n1 + 1/n2))
            t_stat = (mean1 - mean2) / pooled_se
            df = n1 + n2 - 2

            if alternative == "μ₁ ≠ μ₂ (Two-tailed)":
                p_value = 2 * (1 - t.cdf(abs(t_stat), df))
            elif alternative == "μ₁ > μ₂ (Right-tailed)":
                p_value = 1 - t.cdf(t_stat, df)
            else:
                p_value = t.cdf(t_stat, df)

            st.subheader("🧾 Results")
            st.write(f"T-Statistic: **{t_stat:.4f}**")
            st.write(f"Degrees of Freedom: **{df}**")
            st.write(f"P-Value: **{p_value:.4f}**")

            st.markdown("### 📌 Test Decision Based on P-Value")
            st.table({
                "Significance Level (α)": [alpha],
                "P-Value": [round(p_value, 4)],
                "Decision": ["Reject H₀ ✅" if p_value < alpha else "Do not reject H₀ ❌"]
            })

        except:
            st.error("❌ Please check your input data. It must be comma-separated numeric values.")
