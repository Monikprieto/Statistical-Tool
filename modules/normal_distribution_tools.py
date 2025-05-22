import streamlit as st
from scipy.stats import norm

def run():
    st.header("📊 Normal Distribution Tools")

    option = st.radio("Select calculation type:", [
        "📈 Find P(X ≤ x) or P(X > x)",
        "🎯 Find x given P(X ≤ x)",
        "🔧 Apply continuity correction"
    ])

    if option == "📈 Find P(X ≤ x) or P(X > x)":
        st.subheader("Calculate Probability from X")
        mu = st.number_input("Population Mean (μ)", value=50.0)
        sigma = st.number_input("Population Std Dev (σ)", min_value=0.0001, value=10.0)
        x = st.number_input("Value of X", value=60.0)

        z = (x - mu) / sigma
        p_less = norm.cdf(z)
        p_greater = 1 - p_less

        st.markdown("### 🔍 Results")
        st.write(f"Z-Score: **{z:.4f}**")
        st.write(f"P(X ≤ {x}) = **{p_less:.4f}**")
        st.write(f"P(X > {x}) = **{p_greater:.4f}**")

    elif option == "🎯 Find x given P(X ≤ x)":
        st.subheader("Find Critical Value x from Probability")
        mu = st.number_input("Population Mean (μ)", value=50.0, key="mu_x")
        sigma = st.number_input("Population Std Dev (σ)", min_value=0.0001, value=10.0, key="sigma_x")
        prob = st.number_input("Desired P(X ≤ x)", min_value=0.0, max_value=1.0, value=0.95)

        z = norm.ppf(prob)
        x = mu + z * sigma

        st.markdown("### 🎯 Results")
        st.write(f"Z-Score: **{z:.4f}**")
        st.write(f"Value x such that P(X ≤ x) = {prob} is: **{x:.4f}**")

    elif option == "🔧 Apply continuity correction":
        st.subheader("Continuity Correction for Discrete to Normal Approximation")
        mu = st.number_input("Mean (μ)", value=11.4)
        sigma = st.number_input("Std Dev (σ)", min_value=0.0001, value=3.6)
        x = st.number_input("Observed value (x)", value=10.0)

        x_low = x - 0.5
        x_high = x + 0.5

        z_low = (x_low - mu) / sigma
        z_high = (x_high - mu) / sigma

        p_low = norm.cdf(z_low)
        p_high = norm.cdf(z_high)
        p_exact = p_high - p_low

        st.markdown("### 🧾 Results")
        st.write(f"Z for x-0.5: **{z_low:.4f}**, P(X < {x}) ≈ **{p_low:.4f}**")
        st.write(f"Z for x+0.5: **{z_high:.4f}**, P(X ≤ {x}) ≈ **{p_high:.4f}**")
        st.write(f"Probability P(X = {x}) ≈ **{p_exact:.4f}**")
