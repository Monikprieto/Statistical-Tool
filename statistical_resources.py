import streamlit as st

def show_resources():
    st.markdown("""
### 📚 Resources and Glossary

This section provides references, acknowledgments, and a glossary of key statistical terms to support understanding and transparency in the use of this tool.

---

### 📖 References and Attribution

The development of this statistical tool was supported by a combination of open-source Python libraries and statistical literature. The following resources were consulted:

- **Python Libraries**:
  - [Pandas](https://pandas.pydata.org/) – Data manipulation and analysis
  - [NumPy](https://numpy.org/) – Numerical operations
  - [SciPy](https://scipy.org/) – Scientific computing and statistical functions
  - [Statsmodels](https://www.statsmodels.org/) – Statistical models and hypothesis testing
  - [Seaborn](https://seaborn.pydata.org/) – Statistical data visualization
  - [Matplotlib](https://matplotlib.org/) – Plotting library
  - [Streamlit](https://streamlit.io/) – Web app framework for data apps

- **Statistical References**:
  - "Statistics for Business and Economics" by Paul Newbold, William Carlson, and Betty Thorne
  - "Practical Statistics for Data Scientists" by Peter Bruce and Andrew Bruce
  - Online materials from Khan Academy, StatQuest, and Towards Data Science

This tool is intended for educational purposes and transparency in data analysis.

---

### 📘 Glossary of Common Terms

**Descriptive Statistics** – Techniques to summarize and describe features of a dataset.

**Mean (Average)** – Sum of values divided by number of observations.

**Median** – Middle value in a sorted dataset.

**Mode** – Most frequently occurring value.

**Standard Deviation** – Measure of data spread around the mean.

**Variance** – Square of the standard deviation.

**Confidence Interval (CI)** – A range of values likely to contain a population parameter.

**P-Value** – Probability of observing a result as extreme as the one obtained, under the null hypothesis.

**Null Hypothesis (H₀)** – Statement of no effect or no difference.

**Alternative Hypothesis (H₁)** – Statement that there is an effect or difference.

**Test Statistic** – Calculated value used to determine whether to reject H₀.

**Alpha (α)** – Significance level; commonly set at 0.05.

**T-Test** – Compares means between two groups.

**Z-Test** – Used when sample size is large and population standard deviation is known.

**ANOVA** – Tests differences between means of three or more groups.

**Chi-Square Test** – Assesses association between categorical variables.

**Correlation Coefficient (r)** – Measures strength and direction of a linear relationship.

**Outlier** – A value significantly different from others in the dataset.

**Sample** – A subset of the population.

**Population** – The entire group being studied.

---

For further information or full documentation, contact the developer or consult the statistical texts listed above.
    """)
