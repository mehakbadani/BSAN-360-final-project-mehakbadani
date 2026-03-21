# %% [markdown]
# # Lab 6: Credit Approval Analysis
#
# In this assignment, you will analyze the **Japanese Credit Screening** dataset from the UCI Machine Learning Repository. You will perform data cleaning, imputation, type conversion, and consistency checks using `pandas`.
#
# **Objective:** Prepare a raw dataset for analysis by handling missing values, outliers, and incorrect data types.

# %%
# --- Import Libraries ---
import pandas as pd
import numpy as np

# %% [markdown]
# ## Part 1: Loading and Cleaning
# The dataset lacks headers and uses '?' to denote missing values. You need to load it correctly and remove rows with missing critical data.

# %%
# 1. Load 'crx.data' using pd.read_csv
#    Hint: Use header=None and na_values='?'
df = pd.read_csv("crx.data", header=None, na_values='?')

# 2. Drop rows where the Column at Index 1 has a missing value (NaN)

# 3. Save as df_clean

df_clean = df.dropna(subset=[1])

# --- Sanity Check ---
print(df_clean.shape)
# Should be fewer than 690 rows (around 670-680)

# %% [markdown]
# ## Part 2: Imputation
# We still have missing values in other columns. Fill them using the mode (most frequent value).

# %%
# 1. Use df_clean as your starting point
# 2. Iterate through columns or fill them individually using the mode
#    Hint: df[col] = df[col].fillna(df[col].mode()[0])

# 3. Save as df_imputed

df_imputed = df_clean.copy()

# Fill missing values in each column using the mode
for col in df_imputed.columns:
    df_imputed[col] = df_imputed[col].fillna(df_imputed[col].mode()[0])


# --- Sanity Check ---
print(df_imputed.isnull().sum().sum())
# Should be 0

# %% [markdown]
# ## Part 3: Column Types
# The dataset currently treats many numeric columns as objects (strings). Enforce strict data types.

# %%
# 1. Use df_imputed as your starting point
# 2. Convert columns to the correct types:
#    - Float: Indices 1, 2, 7
#    - Int: Indices 10, 13, 14
#    - Category: Indices 0, 3, 4, 5, 6, 8, 9, 11, 12, 15

# 3. Save as df_typed

df_typed = df_imputed.copy()

# Float columns
for col in [1, 2, 7]:
    df_typed[col] = df_typed[col].astype(float)

# Int columns
for col in [10, 13, 14]:
    df_typed[col] = df_typed[col].astype(int)

# Category columns
for col in [0, 3, 4, 5, 6, 8, 9, 11, 12, 15]:
    df_typed[col] = df_typed[col].astype("category")

# --- Sanity Check ---
print(df_typed.dtypes)
# Check that Indices 1, 2, 7, 10, 13, 14 are NOT 'object'

# %% [markdown]
# ## Part 4: Data Consistency
# Columns at Index 3 and Index 4 imply each other. Remove the redundant one.

# %%
# 1. Use df_typed as your starting point
# 2. Drop the Column at Index 4

# 3. Save as df_consistent

df_consistent = df_typed.drop(columns=[4])


# --- Sanity Check ---
print(df_consistent.shape[1])
# Should be 15 columns

# %% [markdown]
# ## Part 5: Outliers
# Filter out rows with extreme values in Indices 13 and 14.

# %%
# 1. Use df_consistent as your starting point
# 2. Keep only rows where:
#    - Column at Index 14 < 50000
#    - AND
#    - Column at Index 13 < 1000

# 3. Save as df_no_outliers

df_no_outliers = df_consistent[
    (df_consistent[14] < 50000) &
    (df_consistent[13] < 1000)
]

# %% [markdown]
# ## Part 6: Sampling
# Create a random sample for manual review.

# %%
# 1. Take a sample of 50 applicants from df_no_outliers
#    CRITICAL: Use random_state=42

# 2. Save as final_sample

final_sample = final_sample = df_no_outliers.sample(n=50, random_state=42)

print(final_sample.shape)

# print(final_sample.shape)
