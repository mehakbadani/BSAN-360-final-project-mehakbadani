# %% [markdown]
# # Hands-on Exercise 10: Data Aggregation and Group Operations
#
# In this assignment, you will practice data aggregation and group operations using the `mtcars` dataset.
#
# **Crucial Autograder Rule:**
# This assignment is graded automatically. The grader checks the **values of specific variables** in your code.
# * **Do not change the variable names** specified in the instructions.
# * Ensure your final results are assigned to the exact variable names provided in the starter code.

# %% [markdown]
# ## Part 1: Grouping Data (1 Point)
#
# ### 1. Setup
# 1. Import `pandas` as `pd`.
# 2. Load the `mtcars.csv` dataset into a DataFrame called `df`.

# %%
# 1. Setup
import pandas as pd

# Load the dataset
df = pd.read_csv('mtcars.csv')
df.head()

# %% [markdown]
# ### 2. Grouping Objects (0.25 Points)
# 1. Group the rows of the data frame by the number of cylinders (`cyl`).
# 2. Save the grouped object in a variable called `grouped_cyl`.

# %%
# Write your code below. Do not change the variable name 'grouped_cyl'.

grouped_cyl = df.groupby("cyl")


# %% [markdown]
# ### 3. Count Objects (0.25 Points)
# 1. How many cars are in each group?
# 2. Save this Series in a variable called `cyl_counts`.

# %%
# Write your code below. Do not change the variable name 'cyl_counts'.

cyl_counts = grouped_cyl.size()
cyl_counts

# %% [markdown]
# ### 4. Information for 4-cylinder Cars (0.25 Points)
# 1. Print all the information you have about 4-cylinder cars.
# 2. Save this DataFrame in a variable called `cyl_4_info`.

# %%
# Write your code below. Do not change the variable name 'cyl_4_info'.

cyl_4_info = df[df["cyl"] == 4]
cyl_4_info

# %% [markdown]
# ### 5. Minimum and Maximum MPG (0.25 Points)
# 1. For each group, show the minimum and maximum miles/gallon (`mpg`).
# 2. Save this DataFrame in a variable called `cyl_mpg_stats`.

# %%
# Write your code below. Do not change the variable name 'cyl_mpg_stats'.

cyl_mpg_stats = grouped_cyl["mpg"].agg(["min", "max"])
cyl_mpg_stats

# %% [markdown]
# ## Part 2: Example: Imputing Missing Data by Group Means (0.5 Points)
# *Note: There is no missing data in this data set, so we will replace the existing data instead.*
#
# 1. Write a function called `replace_median` that:
#     * takes a group as its input
#     * sets all the values in the group’s `hp` column equal to the median of the group’s `hp` values
#     * Returns the group.
# 2. Using `apply()`, call `replace_median` on the groups from Part 1.
# 3. Save the resulting DataFrame in a variable called `imputed_df`.

# %%
# Write your function below. Do not change the function name 'replace_median'.


def replace_median(group):
    median_hp = group["hp"].median()
    group["hp"] = median_hp
    return group


# Apply the function and save the result. Do not change the variable name 'imputed_df'.
imputed_df = imputed_df = grouped_cyl.apply(replace_median)

imputed_df

# %% [markdown]
# ## Part 3: Pivot Tables (0.25 Points)
# Three of the other columns are `qsec` (time to ¼ mile), `vs` (0 if engine is v-shaped, 1 otherwise), `am` (0 if automatic transmission, 1 if manual).
#
# 1. Build a pivot table displaying the median `qsec` for each `vs` and `am`.
# 2. Save this DataFrame in a variable called `qsec_pt`.

# %%
# Write your code below. Do not change the variable name 'qsec_pt'.

qsec_pt = qsec_pt = pd.pivot_table(
    df, values="qsec", index="vs", columns="am", aggfunc="median")
qsec_pt

# %% [markdown]
# ## Part 4: Cross-Tabulation (0.25 Points)
# 1. Build a crosstab showing how many cars are in each `vs` / `am` combination.
# 2. Save this DataFrame in a variable called `vs_am_ct`.

# %%
# Write your code below. Do not change the variable name 'vs_am_ct'.

vs_am_ct = pd.crosstab(df["vs"], df["am"])
vs_am_ct
