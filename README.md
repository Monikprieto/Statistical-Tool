📊 README – Statistical Tool (Cloud Version)

An interactive, modular statistical analysis tool built in **Python** and **Streamlit**, designed to simplify the execution and interpretation of classical and modern statistical tests.

---

## 1. 📘 Introduction

This project presents a fully interactive web-based tool for statistical analysis. It allows students, analysts, and professionals to perform hypothesis testing, ANOVA, regression, correlation, outlier detection, and probability simulations **without needing to write code**.

Each test is implemented as a modular component, and the tool includes example datasets and visual outputs to guide users in learning and decision-making.

---

## 2. 📁 Dataset Description

The app accepts custom `.csv` files and provides a set of **preloaded templates** for quick testing:

- `descriptive_template.csv`
- `ztest_template.csv`
- `ttest_template.csv`
- `proportion_test_template.csv`
- `chi_square_template.csv`
- `correlation_template.csv`
- `sampling_template.csv`
- `linear_regression_template.csv`
- `logistic_regression_template.csv`
- `encoding_template.csv`
-    ...

These templates ensure that each module receives well-formatted inputs for consistent analysis.

---

## 3. 🛠️ Tools and Technologies

| Component        | Description                                   |
|------------------|-----------------------------------------------|
| Language         | Python 3.x                                     |
| Web Framework    | [Streamlit](https://streamlit.io)              |
| Data Handling    | `pandas`, `numpy`                              |
| Stats Engine     | `scipy`, `statsmodels`                         |
| Visualization    | `matplotlib`, `seaborn`                        |
| Export & Support | PDF/Excel export, glossary, statistical tables|

---

## 4. ⚙️ Procedure Overview

### ✔️ How it works:

1. **Upload your dataset** (or use a template).
2. **Choose a statistical module** from the sidebar.
3. **Select variables and parameters** interactively.
4. **Run the analysis** and visualize the results.
5. **Export results** to PDF or Excel (if available).

### 🔎 Each module includes:

- Data validation
- Test execution (Z, T, F, Chi², ANOVA, regression)
- P-value and statistical decision logic
- Confidence intervals, post-hoc tests
- Dynamic plots
- Result interpretation

---

## 5. 🏗️ High-Level Architecture

                        +-----------------------+
                        |    🌐 Web Interface    |
                        |   (Streamlit Frontend)|
                        +----------+------------+
                                   |
                          User selects analysis,
                          uploads file, sets params
                                   ↓
         ┌─────────────────────────────────────────────────────┐
         │                    🎛️ App Core (app.py)              │
         │ - Renders sidebar and navigation menu               │
         │ - Routes user actions to appropriate modules        │
         │ - Manages session state, input, and rendering       │
         └─────────────────────────────────────────────────────┘
                                   ↓
                      +------------+-------------+
                      |                          |
          +-----------v------------+  +----------v----------+
          |     📁 Modules (Test)  |  |  📦 Utility Modules  |
          |  /modules/*.py        |  |  - PDF/Excel Export  |
          |                       |  |  - Reference Tables  |
          |  - Hypothesis Tests   |  |  - Interpretation    |
          |  - ANOVA              |  |  - Dataset Templates |
          |  - Correlation        |  +----------------------+
          |  - Regression         |
          |  - Probability Tools  |
          |  - Encoding / Outliers|
          +-----------+-----------+
                      ↓
         +------------+------------+
         |     📊 Stats Engine     |
         | (pandas, scipy, statsmodels) |
         |  - Data processing      |
         |  - Z, T, F, χ² tests    |
         |  - Regression models    |
         |  - Confidence intervals |
         +------------+------------+
                      ↓
         +------------+------------+
         |   📈 Visualization Layer |
         |  (matplotlib, seaborn)  |
         |  - Boxplots, Histograms |
         |  - Heatmaps, ANOVA plots|
         |  - Confidence curves    |
         +-------------------------+

---

📁 Project Structure

The project has been updated to support deployment on Streamlit Cloud. It now follows this structure:

- Statistical-Tool/
  ├── app.py
  ├── statistical_tables.py
  ├── assets/
  │   ├── css/
  │   │   └── style.css
  │   ├── tables/
  │   │   ├── z-table.pdf
  │   │   ├── t-table.pdf
  │   │   ├── F-table.pdf
  │   │   ├── chi-square-table.pdf
  │   │   ├── Pearsonstable.pdf
  │   │   ├── Binomial-Distribution-Table.pdf
  │   │   ├── poisson_table.pdf
  │   │   └── Standard-Normal-Ztable.pdf


🚀 Deployment Adaptations for Streamlit Cloud

To ensure compatibility with Streamlit Cloud:
- All PDF visualizations have been adapted using a function that displays a download button and, when running locally, renders the PDF in an iframe using base64.
- When hosted on the cloud, the app skips inline rendering and only shows a secure download link (iframe embedding is not supported directly).
- `st.secrets` was replaced with `st.get_option('server.baseUrlPath')` to dynamically retrieve the relative URL path on cloud.
- Local checks now use `st.query_params.get("host", [""])[0]` (previously deprecated `experimental_get_query_params`).

## 7. ✅ Results

Each module generates:
- Test statistics, confidence intervals
- p-values and decision conclusions
- Interpretable charts and tables
- Clear visual markers for hypothesis rejection
- Matching results with manual examples for validation

---

## 8. 📌 Conclusion

This statistical tool integrates essential analytical methods in an intuitive, modular format. Designed for teaching, learning, and practical data exploration, it offers:

- Guided input templates
- Real-time interactive results
- Expandable architecture (via `/modules`)
- Support for classic and inferential statistics

### 🚀 Future Enhancements

- Machine learning module integration  
- Unified PDF report generator  
- Full bilingual support (English/Spanish)

---

🎯 Usage

Once deployed, the app allows users to:
- Upload CSV files.
- Perform various statistical analyses (Z, T, F, Chi-square, etc.).
- Reference visual and downloadable statistical tables.
- Access a custom UI styled with `/assets/css/style.css`.

📄 Custom CSS

The app loads a custom CSS style using:
```
with open("assets/css/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
```

✅ Final Notes

This version of the project is fully adapted for cloud deployment and verified at:  
https://statistical-tool-mp.streamlit.app/

## Contact
Developed by **Mónica Prieto** 
