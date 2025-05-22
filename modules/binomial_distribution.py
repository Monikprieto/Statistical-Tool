import streamlit as st
from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np

def run():
    st.header("🎯 Binomial Distribution Calculator")

    st.markdown("Use this module to compute probabilities and visualize the binomial distribution.")

    n = st.number_input("Number of trials (n)", min_value=1, step=1, value=10)
    p = st.number_input("Probability of success (p)", min_value=0.0, max_value=1.0, value=0.5)
    x = st.number_input("Target value (x)", min_value=0, step=1, value=5)

    calc_type = st.radio("Select Probability Type", [
        "P(X = x)",
        "P(X ≤ x)",
        "P(X ≥ x)"
    ])

    if calc_type == "P(X = x)":
        prob = binom.pmf(x, n, p)
    elif calc_type == "P(X ≤ x)":
        prob = binom.cdf(x, n, p)
    else:
        prob = 1 - binom.cdf(x - 1, n, p)

    st.markdown("### 📊 Result")
    st.write(f"**{calc_type} = {prob:.4f}**")

    st.markdown("### 📈 Binomial Distribution Plot")
    x_vals = np.arange(0, n+1)
    y_vals = binom.pmf(x_vals, n, p)

    fig, ax = plt.subplots(figsize=(15, 5))
    bars = ax.bar(x_vals, y_vals, color="lightblue", edgecolor="black")
    if 0 <= x <= n:
        bars[int(x)].set_color("orange")

    ax.set_title("Binomial Distribution (n={}, p={})".format(n, p))
    ax.set_xlabel("Number of Successes")
    ax.set_ylabel("Probability")
    st.pyplot(fig)
