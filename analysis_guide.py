import streamlit as st

def show_analysis_guide():
    st.markdown("""
### Descriptive Analysis
Summarizes and describes the main characteristics of a dataset. Helps understand the distribution, central tendency, and dispersion before applying more complex tests.

**Requirements:**
- One or more numeric or categorical columns.
- Data without missing values.
- Can include mean, median, mode, standard deviation, min, max, percentiles, and plots.

---

### Sampling
Extracts a representative sample from a larger dataset. Useful when analyzing the full population is costly or unnecessary.

**Requirements:**
- Complete dataset (population).
- Desired sample size.
- Option for simple, stratified, or systematic sampling (with or without replacement).

---

### Hypothesis Testing

**T-Test (Two Groups)**
Compares if there is a significant difference between the means of two independent groups.

**Requirements:**
- Two independent samples with numeric values.
- Assumes approximately normal distribution.
- Required columns: group 1 and group 2 numeric data.

**Z-Test (Sample vs Population)**
Compares a sample mean to a known population mean when population standard deviation is known. For large samples (n ≥ 30).

**Requirements:**
- Numeric sample.
- Known population mean.
- Known population standard deviation.
- Sample size ≥ 30.

**One-Way ANOVA**
Compares the means of three or more independent groups to determine if at least one differs significantly.

**Requirements:**
- One categorical variable (group labels).
- One numeric variable (values to compare).
- Required columns: group and value.

**Two-Way ANOVA**
Examines how two independent factors affect a dependent variable. Detects interaction effects.

**Requirements:**
- Two categorical variables (factors).
- One numeric outcome variable.
- Required columns: factor A, factor B, and values.

**Tukey HSD (Post-Hoc)**
Moved inside Hypothesis module. Used after a significant ANOVA result to identify which specific group pairs differ.

**Requirements:**
- Significant result in one-way ANOVA.
- One categorical variable (groups).
- One numeric variable (measured values).
- Required columns: group and value.

---

### Correlation
Measures strength and direction of the relationship between two variables. Includes:
- **Pearson** for linear correlation
- **Spearman** for monotonic relationships
- **Kendall** for ordinal associations
- **Point-Biserial** for binary-continuous comparisons
- **Chi-Square Phi** for two binary categorical variables

**Requirements:**
- At least two numeric or binary columns.

---

### Chi-Square Test
Analyzes relationships between categorical variables. Useful for testing independence (e.g., gender vs product preference).

**Requirements:**
- Contingency table with counts.
- Two categorical variables.
- Data arranged in crossed categories.

---

### Proportion Test
Tests if the observed proportion in one or two groups differs significantly from a theoretical value or between each other.

**One Proportion:**
- Compare one group proportion against a known value.
- Required: single binary column.

**Two Proportions:**
- Compare proportions between two independent groups.
- Required: binary outcome + grouping column.

**Fisher Exact Test:**
- For small sample sizes (2x2 table).
- Required: two categorical columns forming a 2x2 contingency table.

---

### Linear Regression
Models the linear relationship between an independent variable (X) and a dependent variable (Y).

**Requirements:**
- One numeric predictor column.
- One numeric response column.
- Clean dataset with numeric values only.

---

### Logistic Regression
Models the probability of a binary outcome using one numeric predictor.

**Requirements:**
- One numeric predictor column.
- One binary (0/1) outcome column.
- Clean and properly encoded dataset.

---

### Outliers Analysis
Identifies extreme values using statistical methods such as Z-score and IQR. Helps detect potential data issues.

**Requirements:**
- One numeric column.
- Clean data without nulls.
- Can apply Z-Score or IQR thresholds.

---

### Categorical Encoding
Transforms categorical data into numeric formats for use in modeling (e.g., regression, classification).

**Methods:**
- One-Hot Encoding: creates binary columns for each category.
- Label Encoding: assigns an integer to each unique category.

**Requirements:**
- One or more categorical columns.
- Clean dataset without nulls.
    """)
