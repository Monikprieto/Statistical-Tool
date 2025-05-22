
import streamlit as st
from scipy.stats import norm
import numpy as np

def run():
    st.header("🧮 Z-Test for One Proportion")

    st.markdown("Use this test to compare an observed sample proportion to a known population proportion.")

    with st.form("one_prop_form"):
        st.subheader("Enter Sample and Population Data")

        x = st.number_input("Number of Successes in Sample (x)", min_value=0, step=1, value=45)
        n = st.number_input("Sample Size (n)", min_value=1, step=1, value=100)
        p0 = st.number_input("Expected Population Proportion (p₀)", min_value=0.0, max_value=1.0, value=0.5)

        alpha = st.number_input("Significance Level (α)", min_value=0.01, max_value=0.10, step=0.01, value=0.05)

        alternative = st.selectbox(
            "Alternative Hypothesis (H₁)",
            ["p ≠ p₀ (Two-tailed)", "p > p₀ (Right-tailed)", "p < p₀ (Left-tailed)"]
        )

        submitted = st.form_submit_button("Run One-Proportion Z-Test")

    if submitted:
        p_hat = x / n
        se = np.sqrt(p0 * (1 - p0) / n)
        z_score = (p_hat - p0) / se

        if alternative == "p ≠ p₀ (Two-tailed)":
            p_value = 2 * (1 - norm.cdf(abs(z_score)))
        elif alternative == "p > p₀ (Right-tailed)":
            p_value = 1 - norm.cdf(z_score)
        else:
            p_value = norm.cdf(z_score)

        st.subheader("🧾 Results")
        st.write(f"Observed Proportion (p̂): **{p_hat:.4f}**")
        st.write(f"Z-Score: **{z_score:.4f}**")
        st.write(f"P-Value: **{p_value:.4f}**")

        st.markdown("### 📌 Test Decision Based on P-Value")
        st.table({
            "Significance Level (α)": [alpha],
            "P-Value": [round(p_value, 4)],
            "Decision": ["Reject H₀ ✅" if p_value < alpha else "Do not reject H₀ ❌"]
        })
