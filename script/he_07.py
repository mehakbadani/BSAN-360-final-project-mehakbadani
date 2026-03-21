# %% [markdown]
# # Hands-on Exercise 7: Pandas Data Cleaning & Transformations
#
# In this assignment, you will practice using **pandas** and **numpy** to clean, transform, and prepare a dataset.
#
# **Important:**
# * Follow the instructions in the `README.md` file carefully.
# * **Do not change the variable names** provided in the starter code (e.g., `data`, `df_part2`, `data_final`).
# * The autograder checks specific variables at the end of each part.

# %%
import numpy as np
import pandas as pd

# %% [markdown]
# ## Part 1: Handling Missing Values
#
# We start with a "dirty" dataset containing missing values (`NaN`). Your goal is to clean it.

# %%
# -------------------------------------------------------------------------
# Part 1: Setup (Do not modify this block)
# -------------------------------------------------------------------------
data = pd.DataFrame([
    [1., 6.5, 3.],
    [1., np.nan, np.nan],
    [np.nan, np.nan, np.nan],
    [np.nan, 6.5, 3.],
    ['GHall', 'Bossone', None]
])
data = data.T

# -------------------------------------------------------------------------
# Your Code for Part 1 Below
# -------------------------------------------------------------------------

# 1. Column Dropping
# Identify columns with 2 or more missing values and drop them from `data`.
cols_to_drop = data.columns[data.isna().sum() >= 2]
data = data.drop(columns=cols_to_drop)

# 2. Imputation
# Calculate the mean of Column 3 and fill the missing value in Column 3 with it.
data[3] = pd.to_numeric(data[3], errors='coerce')
mean_col3 = data[3].mean()
data[3] = data[3].fillna(mean_col3)

# 3. Specific Fill
# Replace the missing value in Column 4 with the string 'GHall'.
data[4] = data[4].fillna('GHall')

# 4. Checkpoint
# Save the processed DataFrame in a variable called `data_imputed`.
data_imputed = data
print(data_imputed)

# %% [markdown]
# ## Part 2: Data Transformations
#
# To ensure everyone starts with the same data, we will use a fresh DataFrame (`df_part2`) for this section.

# %%
# -------------------------------------------------------------------------
# Part 2: Setup (Do not modify this block)
# -------------------------------------------------------------------------
df_part2 = pd.DataFrame({
    'length': [1.0, 6.5, 3.0],
    'width': [4.75, 6.5, 3.0],
    'building': ['GHall', 'Bossone', 'GHall']
})

# -------------------------------------------------------------------------
# Your Code for Part 2 Below
# -------------------------------------------------------------------------

# 1. Type Conversion
# Ensure 'length' and 'width' are floats. Convert 'building' to category.
df_part2["length"] = df_part2["length"].astype(float)
df_part2["width"] = df_part2["width"].astype(float)
df_part2["building"] = df_part2["building"].astype("category")

# 2. Unit Conversion
# Create a new column 'width_yds' (width / 3).
df_part2["width_yds"] = df_part2["width"] / 3

# 3. Binning
# Create 'length_cat' using pd.cut with bins [0, 1.5, 4, np.inf].
# Labels should be: 'Short', 'Medium', 'Long'.
df_part2["length_cat"] = pd.cut(
    df_part2["length"],
    bins=[0, 1.5, 4, np.inf],
    labels=["Short", "Medium", "Long"]
)

# (Note: The autograder will check `df_part2` directly for these changes)
print(df_part2.info())

# %% [markdown]
# ## Part 3: Filtering & Dummy Variables
#
# We use another fresh DataFrame (`df_part3`) to test your filtering logic independently.

# %%
# -------------------------------------------------------------------------
# Part 3: Setup (Do not modify this block)
# -------------------------------------------------------------------------
df_part3 = pd.DataFrame({
    'length': [1.0, 6.5, 3.0],
    'width_yds': [1.583, 2.166, 1.0],
    'building': ['GHall', 'Bossone', 'GHall']
})

# -------------------------------------------------------------------------
# Your Code for Part 3 Below
# -------------------------------------------------------------------------

# 1. Filtering
# Filter `df_part3` to keep rows where length >= 2 AND width_yds >= 1.
# Save the result as `data_final`.
data_final = df_part3[
    (df_part3["length"] >= 2) &
    (df_part3["width_yds"] >= 1)
]


# 2. Dummy Variables
# Create dummy variables for the 'building' column in `data_final`.
# Save the result as `bldg_dummies`.
bldg_dummies = pd.get_dummies(data_final["building"])

print(data_final)
print(bldg_dummies)
