
import streamlit as st
from scipy.stats import t
import numpy as np

def run():
    st.header("📊 T-Test for Independent Samples (Unequal Variances)")

    st.markdown("Use this test when population variances are **not equal**.")

    with st.form("t_test_unequal_var_form"):
        st.subheader("Enter Sample Data")

        data1 = st.text_area("Sample 1 Data (comma-separated)", "561,295,299,319,314,324,288,367,207,333")
        data2 = st.text_area("Sample 2 Data (comma-separated)", "370,525,317,625,373,492,803,476,263,367")

        alpha = st.number_input("Significance Level (α)", min_value=0.01, max_value=0.10, step=0.01, value=0.05)

        alternative = st.selectbox(
            "Alternative Hypothesis (H₁)",
            ["μ₁ ≠ μ₂ (Two-tailed)", "μ₁ > μ₂ (Right-tailed)", "μ₁ < μ₂ (Left-tailed)"]
        )

        submitted = st.form_submit_button("Run Welch's T-Test")

    if submitted:
        try:
            x1 = np.array([float(i.strip()) for i in data1.split(",")])
            x2 = np.array([float(i.strip()) for i in data2.split(",")])

            n1, n2 = len(x1), len(x2)
            mean1, mean2 = np.mean(x1), np.mean(x2)
            var1, var2 = np.var(x1, ddof=1), np.var(x2, ddof=1)

            se = np.sqrt(var1/n1 + var2/n2)
            t_stat = (mean1 - mean2) / se

            df = (var1/n1 + var2/n2)**2 / ((var1**2)/((n1**2)*(n1-1)) + (var2**2)/((n2**2)*(n2-1)))

            if alternative == "μ₁ ≠ μ₂ (Two-tailed)":
                p_value = 2 * (1 - t.cdf(abs(t_stat), df))
            elif alternative == "μ₁ > μ₂ (Right-tailed)":
                p_value = 1 - t.cdf(t_stat, df)
            else:
                p_value = t.cdf(t_stat, df)

            st.subheader("🧾 Results")
            st.write(f"T-Statistic: **{t_stat:.4f}**")
            st.write(f"Degrees of Freedom: **{df:.2f}**")
            st.write(f"P-Value: **{p_value:.4f}**")

            st.markdown("### 📌 Test Decision Based on P-Value")
            st.table({
                "Significance Level (α)": [alpha],
                "P-Value": [round(p_value, 4)],
                "Decision": ["Reject H₀ ✅" if p_value < alpha else "Do not reject H₀ ❌"]
            })

        except:
            st.error("❌ Please check your input data. It must be comma-separated numeric values.")
