import streamlit as st
import os
from glob import glob

# NUEVA FUNCION PARA IMAGEN + PDF

def show_table_multi(image_folder, pdf_path, label):
    image_files = sorted(glob(os.path.join(image_folder, "*.png")))

    if image_files:
        for img in image_files:
            st.image(img, use_column_width=True)
    else:
        st.warning(f"⚠️ No images found in: {image_folder}")

    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as f:
            st.download_button(
                f"📥 Download {label} (PDF)",
                data=f,
                file_name=os.path.basename(pdf_path),
                mime="application/pdf"
            )
    else:
        st.error(f"❌ PDF not found: {pdf_path}")

def main():
    st.title("\U0001F4CA Statistical Tables Reference")

    tab_names = [
        "Z Table", "T Table", "F Table", "Chi-Square",
        "Pearson Correlation", "Binomial", "Poisson",
        "Normal Dist", "Exponential", "Two-sample T", 
    ]

    tabs = st.tabs(tab_names)

    with tabs[0]:
        st.subheader("Z Table")
        st.markdown("""
**Use Cases:**  
- Used for the standard normal distribution.  
- Applied when population standard deviation is known or n ≥ 30.  
- Symmetric with μ = 0 and σ = 1.

**Example:** Confidence intervals, hypothesis tests for means with known σ.

**Key Formulas:**  
- Critical Z: `=NORM.S.INV(1 - α/2)`  
- Cumulative Probability: `=NORM.S.DIST(Z, TRUE)`
        """)
        show_table_multi("assets/images/Z-Table/", "assets/tables/Standard-Normal-Ztable.pdf", "Z Table")

    with tabs[1]:
        st.subheader("T Table")
        st.markdown("""
**Use Cases:**  
- Small samples (n < 30) and unknown σ.  
- Longer tails than Z.  
- Depends on degrees of freedom (df = n - 1).

**Example:** Confidence intervals or T-tests for small samples.

**Key Formulas:**  
- Critical T: `=T.INV.2T(α, df)`  
- Cumulative Probability: `=T.DIST(T, df, TRUE)`
        """)
        show_table_multi("assets/images/T-Table/", "assets/tables/t-table.pdf", "T Table")

    with tabs[2]:
        st.subheader("F Table")
        st.markdown("""
**Use Cases:**  
- Comparing variances.  
- Common in ANOVA.

**Degrees of Freedom:** numerator (df1), denominator (df2).

**Example:** Compare group means using ANOVA.

**Key Formulas:**  
- Critical F: `=F.INV.RT(α, df1, df2)`  
- Cumulative Probability: `=F.DIST.RT(F, df1, df2)`
        """)
        show_table_multi("assets/images/F-Table/", "assets/tables/F-table.pdf", "F Table")

    with tabs[3]:
        st.subheader("Chi-Square Table")
        st.markdown("""
**Use Cases:**  
- Independence tests (categorical variables).  
- Goodness-of-fit tests.  
- Homogeneity tests.

**Degrees of Freedom:** Usually categories - 1.

**Example:** Check if observed candy color distribution matches expected.

**Key Formulas:**  
- Critical χ²: `=CHIINV(α, df)`  
- Cumulative Probability: `=CHIDIST(χ², df)`
        """)
        show_table_multi("assets/images/Chi-Square-Table/", "assets/tables/chi-square-table.pdf", "Chi-Square Table")

    with tabs[4]:
        st.subheader("Pearson Correlation Table")
        st.markdown("""
**Use Cases:**  
- Significance of correlation between two continuous variables.

**Degrees of Freedom:** n - 2.

**Example:** Hours studied vs. exam score correlation.

**Key Formulas:**  
- Pearson r: `=CORREL(range1, range2)`  
- Associated T: `=T.INV.2T(α, n - 2)`
        """)
        show_table_multi("assets/images/Pearsonstable/", "assets/tables/Pearsonstable.pdf", "Pearson Table")

    with tabs[5]:
        st.subheader("Binomial Distribution Table")
        st.markdown("""
**Use Cases:**  
- Experiments with two outcomes (success/failure).

**Example:** Probability of 3 heads in 5 coin tosses.

**Key Formulas:**  
- Exact success: `=BINOM.DIST(x, n, p, FALSE)`  
- Cumulative: `=BINOM.DIST(x, n, p, TRUE)`
        """)
        show_table_multi("assets/images/Binomial-Distribution-Table/", "assets/tables/Binomial-Distribution-Table.pdf", "Binomial Table")

    with tabs[6]:
        st.subheader("Poisson Distribution Table")
        st.markdown("""
**Use Cases:**  
- Modeling rare events over time/space.

**Example:** 4 emergency calls per hour if avg = 2.

**Key Formulas:**  
- Exact event count: `=POISSON.DIST(x, λ, FALSE)`  
- Cumulative: `=POISSON.DIST(x, λ, TRUE)`
        """)
        show_table_multi("assets/images/Poisson-Table/", "assets/tables/poisson_table.pdf", "Poisson Table")

    with tabs[7]:
        st.subheader("Normal Distribution (Z-Score)")
        st.markdown("""
**Use Cases:**  
- For percentiles or probability under the normal curve.

**Example:** Prob. a value falls below X with known μ and σ.

**Key Formula:**  
- Cumulative Probability: `=NORM.DIST(X, mean, std_dev, TRUE)`
        """)
        show_table_multi("assets/images/Z-table-NormalDist/", "assets/tables/z-table.pdf", "Normal Z Table")

    with tabs[8]:
        st.subheader("Exponential Distribution Table")
        st.markdown("""
**Use Cases:**  
- Time until the next event in Poisson processes.

**Example:** Prob. a product fails within a given time.

**Key Formula:**  
- Cumulative: `=EXPON.DIST(x, λ, TRUE)`
        """)
        st.warning("⚠️ Exponential table not yet available.")

    with tabs[9]:
        st.subheader("Two-Sample T Table")
        st.markdown("""
**Use Cases:**  
- Comparing two independent sample means.

**Example:** Compare exam scores of two student groups.

**Key Formula:**  
- `=T.TEST(range1, range2, tails, type)`
  - tails: 1 or 2  
  - type: 1 = paired, 2 = equal variances, 3 = unequal
        """)
