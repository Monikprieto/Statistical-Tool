import streamlit as st
import math

def run():
    st.header("🔢 Combinatorics & Sample Spaces")

    st.markdown("This module helps you calculate permutations and combinations.")

    calc_type = st.radio("Choose calculation type:", [
        "Permutations (nPr)",
        "Combinations (nCr)",
        "Sample Space Size (n outcomes, k steps)"
    ])

    if calc_type in ["Permutations (nPr)", "Combinations (nCr)"]:
        n = st.number_input("Total number of items (n)", min_value=1, step=1, value=5)
        r = st.number_input("Number of selections (r)", min_value=0, max_value=100, step=1, value=3)

        if calc_type == "Permutations (nPr)":
            if r > n:
                st.warning("r must be less than or equal to n.")
            else:
                result = math.perm(int(n), int(r))
                st.markdown(f"### 📊 Result: **{int(n)}P{int(r)} = {result}**")

        elif calc_type == "Combinations (nCr)":
            if r > n:
                st.warning("r must be less than or equal to n.")
            else:
                result = math.comb(int(n), int(r))
                st.markdown(f"### 📊 Result: **{int(n)}C{int(r)} = {result}**")

    elif calc_type == "Sample Space Size (n outcomes, k steps)":
        n = st.number_input("Number of possible outcomes per step (n)", min_value=1, step=1, value=2)
        k = st.number_input("Number of steps (k)", min_value=1, step=1, value=3)

        result = n ** k
        st.markdown(f"### 🧮 Total Sample Space Size: **{n}^ {k} = {result}**")

    st.markdown("---")
    st.markdown("### ℹ️ Notes:")
    st.markdown("- **nPr:** Ordered arrangements of r items from n.")
    st.markdown("- **nCr:** Unordered selections of r items from n.")
    st.markdown("- **Sample space:** Used when evaluating compound experiments (like flipping coins).")
