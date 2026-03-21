# %% [markdown]
# # Hands-on Exercise 8: String Manipulation & Data Wrangling
#
# In this assignment, you will practice string manipulation, combining datasets (merging/concatenating), and reshaping data (pivoting/stacking) using **pandas**.
#
# **Important:**
# * Follow the instructions in the `README.md` file carefully.
# * **Do not change the variable names** provided in the starter code (e.g., `states_cleaned`, `merge_inner`, `grades_long`).
# * The autograder checks specific variables at the end of each part.

# %%
import numpy as np
import pandas as pd

# %% [markdown]
# ## Part 1: Processing Strings (split, strip, replace)
#
# We start with raw product entry from an inventory system that is formatted poorly:

# %%
# -------------------------------------------------------------------------
# Part 1: Setup (Do not modify this block)
# -------------------------------------------------------------------------

raw_entry = " Item# 5001 - Apple "

# -------------------------------------------------------------------------
# Your Code for Part 1 Below
# -------------------------------------------------------------------------

# Extract Product Name
# Split the string `raw_entry` using the hyphen ("-") as the delimiter and save the resulting list to a variable.
# Access the second element of that list (the product name) and remove any leading/trailing whitespace from this text.

product_name = raw_entry.split("-")[1].strip()


# 2. Extract Product ID
# Access the **first element** of your list (the ID) from your split list and remove the substring `"Item#` from this text.
# Remove any remaining leading/trailing whitespace from this text.

product_id = raw_entry.split("-")[0].replace("Item#", "").strip()

# self check
print(f"Product Name: '{product_name}'")
print(f"Product ID: '{product_id}'")

# %% [markdown]
# ## Part 2: Combining and Merging
#
# We will use two DataFrames, `left` and `right`, to practice different merge types and concatenation.

# %%
# -------------------------------------------------------------------------
# Part 2: Setup (Do not modify this block)
# -------------------------------------------------------------------------
np.random.seed(0)
left = pd.DataFrame(
    {'lkey': ['A', 'B', 'C', 'D'], 'value': np.random.randn(4)})
right = pd.DataFrame(
    {'rkey': ['B', 'D', 'E', 'F'], 'value': np.random.randn(4)})

# -------------------------------------------------------------------------
# Your Code for Part 2 Below
# -------------------------------------------------------------------------

# 1. Merging
# Perform Inner, Outer, Left, and Right merges.

merge_inner = pd.merge(left, right, left_on="lkey",
                       right_on="rkey", how="inner")
merge_outer = pd.merge(left, right, left_on="lkey",
                       right_on="rkey", how="outer")
merge_left = pd.merge(left, right, left_on="lkey", right_on="rkey", how="left")
merge_right = pd.merge(left, right, left_on="lkey",
                       right_on="rkey", how="right")


# 2. Concatenating
# Rename keys, add a 'source' column, and stack the DataFrames.
# Save the result as `concat_df`.
left2 = left.rename(columns={"lkey": "key"}).copy()
right2 = right.rename(columns={"rkey": "key"}).copy()

left2["source"] = "left"
right2["source"] = "right"

concat_df = pd.concat([left2, right2], axis=0, ignore_index=True)

print("Inner Merge:\n", merge_inner)
print("\nConcatenated:\n", concat_df)

# %% [markdown]
# ## Part 3: Reshaping and Pivoting
#
# We will use a grade book dataset to practice reshaping data between wide and long formats.

# %%
# -------------------------------------------------------------------------
# Part 3: Setup (Do not modify this block)
# -------------------------------------------------------------------------
grades = pd.DataFrame({
    'Class': ['BSAN 160', 'BSAN 260', 'BSAN 360', 'BSAN 460'],
    'Andy': ['A', None, 'A', 'B+'],
    'Pat': ['B', 'C', 'B', None],
    'James': ['A', 'A', 'A', 'A']
})

# -------------------------------------------------------------------------
# Your Code for Part 3 Below
# -------------------------------------------------------------------------

# 1. Wide to Long
# Reshape so there is one row for each grade (columns: class, student, grade).
# Filter out NaNs. Save as `grades_long`.

grades_long = grades.melt(
    id_vars="Class",
    var_name="student",
    value_name="grade"
).dropna()


# 2. Long to Wide
# Convert `grades_long` back to a wide format (index: class, columns: students).
# Save as `grades_wide`.

grades_wide = grades_long.pivot(
    index="Class",
    columns="student",
    values="grade"
)

print(grades_long)
print(grades_wide)
