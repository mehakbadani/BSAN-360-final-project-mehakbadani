# %% [markdown]
# # Lab Assignment 7: E-Commerce Sales and Logistics Analysis
#
# In this assignment, you will analyze detailed sales data from Olist, a Brazilian company that provides logistics and capital support for small and medium-sized online retailers. The dataset consists of multiple files. Our goal for this week is to combine these datasets in different ways to answer our business questions.
#
# **Objective:** Combine multiple datasets using relational columns to answer targeted business questions.

# %%
# --- Import Libraries ---
import pandas as pd
from scipy.stats import ttest_ind

# --- Load Data ---
# Ensure the Olist_Data folder is in the same directory as this notebook.
customers = pd.read_csv('data_olist/olist_customers_dataset.csv')
items = pd.read_csv('data_olist/olist_order_items_dataset.csv')
payments = pd.read_csv('data_olist/olist_order_payments_dataset.csv')
reviews = pd.read_csv('data_olist/olist_order_reviews_dataset.csv')
orders = pd.read_csv('data_olist/olist_orders_dataset.csv')
products = pd.read_csv('data_olist/olist_products_dataset.csv')
sellers = pd.read_csv('data_olist/olist_sellers_dataset.csv')
category = pd.read_csv('data_olist/product_category_name_translation.csv')

# %% [markdown]
# ## Part 1: High-Value Customers
# **Business Question:** How much did each customer spend on Olist over these 2 years? Who are the “high-value” customers by sales amount?

# %%
# 1. Merge the orders and payments datasets on the order_id column.
df_orders_payments = pd.merge(orders, payments, on='order_id', how='inner')

# 2. Group by customer_id and calculate the sum of the payment_value.
spending = df_orders_payments.groupby('customer_id')['payment_value'].sum()

# --- Sanity Check ---
print(spending.shape)
# Should be 99440 rows

# 3. Merge the spending Series with the customers dataset.
spendloc = pd.merge(customers, spending.reset_index(),
                    on='customer_id', how='inner')

# 4. Sort descending by total spending and extract the top 20 customers.
top_20_customers = spendloc.sort_values(
    by='payment_value', ascending=False).head(20)

# %% [markdown]
# ## Part 2: High-Earning Sellers
# **Business Question:** How much did each seller receive on Olist over these 2 years? Who are the “high-earning” sellers?

# %%
# 1. Group the items dataset by seller_id and calculate the sum of the price.
revenue = items.groupby('seller_id')['price'].sum()


# --- Sanity Check ---
print(revenue.shape)
# Should be 3095 rows

# 2. Merge the revenue Series with the sellers dataset.
df_seller_rev = pd.merge(sellers, revenue.reset_index(),
                         on='seller_id', how='inner')

# 3. Sort descending by total revenue and extract the top 20 sellers.
top_20_sellers = df_seller_rev.sort_values(
    by='price', ascending=False).head(20)

# %% [markdown]
# ## Part 3: Highest Performing Products
# **Business Question:** What types of products have the highest sales volume and highest total sales?

# %%
# 1. Count the number of times each product_id appears. Group by product_id and use .size(). Sort descending.
q3_quant = (
    items.groupby('product_id')
    .size()
    .reset_index(name='quantity')
    .sort_values(by='quantity', ascending=False)
)


# 2. Group the items dataset by product_id and calculate the sum of the price. Sort descending.
q3_value = (
    items.groupby('product_id')['price']
    .sum()
    .reset_index()
    .sort_values(by='price', ascending=False)
)

# 3. Merge the Top 10 rows from q3_quant and the Top 10 rows from q3_value.
highperf = highperf = pd.merge(
    q3_quant.head(10),
    q3_value.head(10),
    on='product_id',
    how='outer'
)

# 4. Merge highperf with products, then merge with category to get the English name.
highperf_final = (
    highperf
    .merge(products[['product_id', 'product_category_name']], on='product_id', how='left')
    .merge(category, on='product_category_name', how='left')
)

highperf_final

# %% [markdown]
# ## Part 4: Delivery Wait Times
# **Business Question:** Are customer reviews influenced by how long it takes for a customer to receive their order?

# %%
# 1. Convert order_delivered_customer_date and order_purchase_timestamp to datetime objects.
# Calculate wait_time (in days) and add it to the 'orders' dataframe.

orders['order_delivered_customer_date'] = pd.to_datetime(
    orders['order_delivered_customer_date'])
orders['order_purchase_timestamp'] = pd.to_datetime(
    orders['order_purchase_timestamp'])

orders['wait_time'] = (orders['order_delivered_customer_date'] -
                       orders['order_purchase_timestamp']).dt.days


# 2. Merge reviews into orders on order_id.
orders_reviews = pd.merge(orders, reviews, on='order_id', how='inner')

# --- Sanity Check ---
print(orders_reviews.shape)
# Should be 99224 rows

# 3. Filter orders_reviews for 1-star reviews and not null wait times.
onestar = orders_reviews[(orders_reviews['review_score'] == 1) & (
    orders_reviews['wait_time'].notna())]

# 4. Filter orders_reviews for 5-star reviews and not null wait times.
fivestar = orders_reviews[(orders_reviews['review_score'] == 5) & (
    orders_reviews['wait_time'].notna())]

# 5. Conduct a two-sample t-test with unequal variances on the wait_time columns.
#    Hint: result = ttest_ind(x, y, equal_var=False)
# Extract the exact p-value.

result = ttest_ind(onestar['wait_time'],
                   fivestar['wait_time'], equal_var=False)

wait_time_p_value = result.pvalue
