
import streamlit as st
from scipy.stats import norm
import numpy as np

def run():
    st.header("📊 Two-Proportion Z-Test")

    st.markdown("Use this test to compare proportions from two independent samples.")

    with st.form("two_prop_z_test_form"):
        st.subheader("Enter Sample Data")

        x1 = st.number_input("Successes in Sample 1 (x₁)", min_value=0, step=1, value=68)
        n1 = st.number_input("Size of Sample 1 (n₁)", min_value=1, step=1, value=80)

        x2 = st.number_input("Successes in Sample 2 (x₂)", min_value=0, step=1, value=72)
        n2 = st.number_input("Size of Sample 2 (n₂)", min_value=1, step=1, value=100)

        alpha = st.number_input("Significance Level (α)", min_value=0.01, max_value=0.10, step=0.01, value=0.05)

        alternative = st.selectbox(
            "Alternative Hypothesis (H₁)",
            ["p₁ ≠ p₂ (Two-tailed)", "p₁ > p₂ (Right-tailed)", "p₁ < p₂ (Left-tailed)"]
        )

        submitted = st.form_submit_button("Run Two-Proportion Z-Test")

    if submitted:
        p1 = x1 / n1
        p2 = x2 / n2

        p_pool = (x1 + x2) / (n1 + n2)
        se = np.sqrt(p_pool * (1 - p_pool) * (1/n1 + 1/n2))

        z_score = (p1 - p2) / se

        if alternative == "p₁ ≠ p₂ (Two-tailed)":
            p_value = 2 * (1 - norm.cdf(abs(z_score)))
        elif alternative == "p₁ > p₂ (Right-tailed)":
            p_value = 1 - norm.cdf(z_score)
        else:
            p_value = norm.cdf(z_score)

        st.subheader("🧾 Results")
        st.write(f"Z-Score: **{z_score:.4f}**")
        st.write(f"P-Value: **{p_value:.4f}**")

        st.markdown("### 📌 Test Decision Based on P-Value")
        st.table({
            "Significance Level (α)": [alpha],
            "P-Value": [round(p_value, 4)],
            "Decision": ["Reject H₀ ✅" if p_value < alpha else "Do not reject H₀ ❌"]
        })
