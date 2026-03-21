# %% [markdown]
# # Lab Assignment 8: Data Visualization
#
# ## Introduction
# In this assignment, you will use Matplotlib and Seaborn to visualize loan application data. The objective is to identify patterns and distributions within continuous and categorical variables using plotting techniques.
#
# **Crucial Autograder Rule:**
# This assignment is graded automatically. The grader checks the **values of specific variables**.
# * **Do not change the variable names** specified in the instructions.
# * If the instructions dictate to save an output or answer in a specific variable, you must use exactly that name.
# * * For multiple choice questions, make sure that you provide the answer as a string (e.g., `answer = "A"`)

# %% [markdown]
# ## Setup
# Run the following cell to import the necessary libraries and load the dataset. Ensure `loans.csv` is in the same directory as this notebook.

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('loans.csv')
df = df.dropna(how='any').copy()
df = df.set_index('loan_id')
df.head()

# %% [markdown]
# ## Part 1: Matplotlib Foundations
#
# ### Setup (1 Point)
# 1. Create a new column named `total_income` by adding the `applicant_income` and `coapplicant_income` columns.
#
# ### Histogram
# 1. Generate a standard histogram of the `total_income` column using `plt.hist()`.
# 2. Generate a second histogram using the `bins` and `range` parameters to filter out extreme outliers (e.g., limit the range to 0 - 20000).
# 3. Add a title and label the x-axis and y-axis.

# %%
# 1. Create total_income column
df["total_income"] = df["applicant_income"] + df["coapplicant_income"]

# 2. Plot standard histogram
plt.figure(figsize=(8, 5))
plt.hist(df["total_income"])
plt.title("Histogram of Total Income")
plt.xlabel("Total Income")
plt.ylabel("Frequency")
plt.show()

# 3. Plot filtered histogram with labels and title
plt.figure(figsize=(8, 5))
plt.hist(df["total_income"], bins=30, range=(0, 20000))
plt.title("Histogram of Total Income (0 to 20000)")
plt.xlabel("Total Income")
plt.ylabel("Frequency")
plt.show()


# %% [markdown]
# ### Scatter plot
# 1. Create a scatter plot using `plt.subplots()`.
# 2. Plot `applicant_income` on the x-axis and `loan_amount` on the y-axis.
# 3. Set the `alpha` parameter to 0.5 to manage overplotting.
# 4. Add appropriate axis labels.

# %%
# Create scatter plot
fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(df["applicant_income"], df["loan_amount"], alpha=0.5)

ax.set_xlabel("Applicant Income")
ax.set_ylabel("Loan Amount")
ax.set_title("Applicant Income vs Loan Amount")

plt.show()


# %% [markdown]
# ## Part 2: Seaborn Statistical Visualization
#
# ### Box Plot
# 1. Use Seaborn to create a box plot (`sns.boxplot`) showing the distribution of `loan_amount` across the different categories of `property_area`.
#
# ### Bar Plot
# 1. Use Seaborn to create a bar plot (`sns.barplot` or `sns.countplot`) displaying the count of **approved** versus **denied loans** (`loan_status`), separated by `gender`.

# %%
# Create box plot
plt.figure(figsize=(8, 5))
sns.boxplot(x="property_area", y="loan_amount", data=df)

plt.title("Loan Amount Distribution by Property Area")
plt.xlabel("Property Area")
plt.ylabel("Loan Amount")
plt.show()

# Create bar plot
plt.figure(figsize=(8, 5))
sns.countplot(x="loan_status", hue="gender", data=df)

plt.title("Loan Status by Gender")
plt.xlabel("Loan Status")
plt.ylabel("Count")
plt.show()

# %% [markdown]
# ## Part 3: Visual Interpretation
# Review the visualizations generated in Part 1 and Part 2. Assign your answers to the designated variables as strings.
#
# ### Histogram Interpretation (1 Point)
# 1. Looking at the initial histogram of `total_income`, how is the data distributed?
# * Positive right-skewed (answer `A`)
# * Negative left-skewed (answer `B`)
# * Normally distributed (answer `C`)
# *Assign your answer to `q1_skewness` (e.g., `q1_skewness = 'A'`).*
#
# ### Scatter Plot Interpretation (1 Point)
# 2. Looking at the scatter plot, what is the visible relationship between `applicant_income` and `loan_amount`?
# * Strong negative correlation (answer `A`)
# * Positive correlation with clustering at the lower income ranges (answer `B`)
# * No visible correlation (answer `C`)
# *Assign your answer to `q2_scatter`.*
#
# ### Bar Plot Interpretation (1 Point)
# 3. Based on the Seaborn bar plot for loan status by gender, what is the visual indication?
# * Males have a visibly higher absolute count of approved loans (answer `A`)
# * The absolute counts of approved loans appear relatively equal between genders (answer `B`)
# * Females have a visibly higher absolute count of approved loans (answer `C`)
# *Assign your answer to `q3_gender_counts`.*
#
# ### Box Plot Interpretation (1 Point)
# 4. Based on the box plot of `loan_amount` by `property_area`, which area exhibits the highest median loan amount?
# * Urban (answer `A`)
# * Semiurban (answer `B`)
# * Rural (answer `C`)
# *Assign your answer to `q4_median_loan`.*

# %%
# Assign your answers as strings (e.g., 'A', 'B', or 'C')

q1_skewness = 'A'

q2_scatter = 'B'

q3_gender_counts = 'A'

q4_median_loan = 'B'
