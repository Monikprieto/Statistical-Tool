import streamlit as st
import base64
import os
import streamlit.components.v1 as components 

def embed_pdf_web_compatible(file_path, label):
    if os.path.exists(file_path):
        # Mostrar botón de descarga
        with open(file_path, "rb") as f:
            st.download_button(f"📥 Download {label}", data=f, file_name=os.path.basename(file_path), mime='application/pdf')

        # Detectar si estamos en local o en la nube
        if "localhost" in st.experimental_get_query_params().get("host", [""])[0] or os.getenv("STREAMLIT_LOCAL") == "1":
            # ✅ Entorno local — usar iframe
            with open(file_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
                pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="500" type="application/pdf"></iframe>'
                st.markdown(pdf_display, unsafe_allow_html=True)
        else:
            # 🌐 Cloud — dar link al PDF si está en /assets/
            base_path = st.get_option('server.baseUrlPath') or ""
            st.markdown(
                f"[📄 View {label} PDF online]({base_path}/assets/tables/{os.path.basename(file_path)})",
                unsafe_allow_html=True
            )

    else:
        st.error(f"❌ {label} not found: {file_path}")

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
        embed_pdf_web_compatible("assets/tables/Standard-Normal-Ztable.pdf", "Z Table")

    with tabs[1]:
        st.subheader("T Table (Student's t)")
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
        embed_pdf_web_compatible("assets/tables/t-table.pdf", "T Table")

    with tabs[2]:
        st.subheader("F Table (Fisher Distribution)")
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
        embed_pdf_web_compatible("assets/tables/F-table.pdf", "F Table")

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
        embed_pdf_web_compatible("assets/tables/chi-square-table.pdf", "Chi-Square Table")

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
        embed_pdf_web_compatible("assets/tables/Pearsonstable.pdf", "Pearson Correlation Table")

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
        embed_pdf_web_compatible("assets/tables/Binomial-Distribution-Table.pdf", "Binomial Table")

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
        embed_pdf_web_compatible("assets/tables/poisson_table.pdf", "Poisson Table")

    with tabs[7]:
        st.subheader("Normal Distribution (Z-Score)")
        st.markdown("""
**Use Cases:**  
- For percentiles or probability under the normal curve.

**Example:** Prob. a value falls below X with known μ and σ.

**Key Formula:**  
- Cumulative Probability: `=NORM.DIST(X, mean, std_dev, TRUE)`
        """)
        embed_pdf_web_compatible("assets/tables/z-table.pdf", "Normal Z Table")

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


