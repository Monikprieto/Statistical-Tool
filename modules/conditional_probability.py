import streamlit as st

def run():
    st.header("🔗 Conditional Probability Calculator")

    st.markdown("Use this tool to compute conditional probabilities using:")
    st.markdown("- **P(A | B) = P(A ∩ B) / P(B)**")
    st.markdown("- Also works for P(B | A) if needed.")

    prob_type = st.selectbox("Select what you want to calculate:", [
        "P(A | B)",
        "P(B | A)"
    ])

    if prob_type == "P(A | B)":
        p_a_and_b = st.number_input("P(A ∩ B)", min_value=0.0, max_value=1.0, value=0.1)
        p_b = st.number_input("P(B)", min_value=0.01, max_value=1.0, value=0.3)
        result = p_a_and_b / p_b
        st.markdown(f"### 📊 Result: **P(A | B) = {result:.4f}**")

    elif prob_type == "P(B | A)":
        p_a_and_b = st.number_input("P(A ∩ B)", min_value=0.0, max_value=1.0, value=0.1)
        p_a = st.number_input("P(A)", min_value=0.01, max_value=1.0, value=0.25)
        result = p_a_and_b / p_a
        st.markdown(f"### 📊 Result: **P(B | A) = {result:.4f}**")

    st.markdown("---")
    st.markdown("### 📘 Notes:")
    st.markdown("- Make sure that the denominator is not zero.")
    st.markdown("- All probabilities must be between 0 and 1.")
    st.markdown("- These are useful in real-world problems involving diagnostics, reliability, and decision-making.")
