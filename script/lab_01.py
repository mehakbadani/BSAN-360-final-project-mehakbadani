# %% [markdown]
# # Lab 1 Assignment: Indego Bike Share Analysis
#
# ## Setup
# **The cell below contains your starter code. Do not modify this cell**
#
# This code imports pandas, loads the data file (`indego-trips-2024-q3.csv`), and creates the list variables you will need for the assignment. Make sure you select the Python kernel with version `3.12`.

# %%
# The pandas library in Python helps with data input/output, cleaning, and transformations.
# We start by loading it and giving it the shorthand pd.
from datetime import datetime
import pandas as pd

# Read in the trip information from the comma-delimited file.
# This returns a Data Frame, which is Python's equivalent of a spreadsheet.
df = pd.read_csv("indego-trips-2024-q3.csv", low_memory=False)

# Create individual lists from the columns of the data frame df.
trip_id = df['trip_id']
duration = df['duration']
start_time = df['start_time']
end_time = df['end_time']
start_station = df['start_station']
start_lat = df['start_lat']
start_lon = df['start_lon']
end_station = df['end_station']
end_lat = df['end_lat']
end_lon = df['end_lon']
bike_id = df['bike_id']
plan_duration = df['plan_duration']
trip_route_category = df['trip_route_category']
passholder_type = df['passholder_type']
bike_type = df['bike_type']

# Let's take a look at the data and some statistics of the numerical columns.
print(df)
print(df.describe())

# %% [markdown]
# ## Part 1: Basic Statistics (1 Point)
# Calculate the total number of trips (`num_trips`) and the average duration (`avg_duration`).

# %%
# Write your code for Part 1 here

num_trips = len(duration)
avg_duration = duration.mean()

# %% [markdown]
# ## Part 2: Indexing & Retrieval (0.5 Points)
# Retrieve details for the **5th** trip: duration (`trip5_duration`), start station (`trip5_start`), and end station (`trip5_end`).

# %%
# Write your code for Part 2 here

trip5_duration = duration[4]
trip5_start = start_station[4]
trip5_end = end_station[4]

# %% [markdown]
# ## Part 3: Datetime Operations (1 Point)
# Calculate the actual duration for the trip at index **1365**. Save the result as a timedelta object named `actual_duration_1365`.

# %%

# Write your code for Part 3 here
start_dt = datetime.strptime(start_time[1365], "%m/%d/%Y %H:%M")
end_dt = datetime.strptime(end_time[1365], "%m/%d/%Y %H:%M")

actual_duration_1365 = end_dt - start_dt

# %% [markdown]
# ## Part 4: Sets & Categories (1 Point)
# Determine the unique values for `trip_route_category`, `passholder_type`, and `bike_type`. Save them as sets named `route_cats`, `pass_types`, and `bike_types`.

# %%
# Write your code for Part 4 here

route_cats = set(trip_route_category)
pass_types = set(passholder_type)
bike_types = set(bike_type)

# %% [markdown]
# ## Part 5: Filtering & Aggregation (1 Point)
# Create filtered lists of durations for each passholder type. Then calculate:
# * `count_monthly`: Number of trips by 'Indego30' holders.
# * `avg_duration_daily`: Average duration for 'Day Pass' holders.
# * `avg_duration_yearly`: Average duration for 'Indego365' holders.

# %%
# Write your code for Part 5 here
monthly = duration[passholder_type == "Indego30"]
daily = duration[passholder_type == "Day pass"]
yearly = duration[passholder_type == "Indego365"]

count_monthly = len(monthly)
avg_duration_daily = daily.mean()
avg_duration_yearly = yearly.mean()

print(count_monthly)

# %% [markdown]
# ## Part 6: Business Recommendation (1 Point)
# Based on Part 5, which group is best suited for 30-40 minute podcasts?
# * "A": Indego365
# * "B": Indego30
# * "C": Day Pass and Walk-up
# * "D": None of them cycles more than 30 minutes
#
# Save your choice (string) in `recommendation`.

# %%
# Write your code for Part 6 here

recommendation = "C"

print(recommendation)
