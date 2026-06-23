# %%
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/SuperMarket.csv")

df.head()

# %%
df.info()

# %%
df.describe()

# %%
sales_by_product = (
    df.groupby("Product line")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

sales_by_product

# %%
sales_by_product.plot(kind="bar")

plt.title("Sales by Product Line")
plt.ylabel("Total Sales")
# plt.show()

plt.savefig("images/sales_by_product.png", bbox_inches="tight")

# %%
branch_sales = (
    df.groupby("Branch")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

branch_sales

# %%
branch_sales.plot(kind="bar")

plt.title("Sales by Branch")
plt.ylabel("Total Sales")
# plt.show()

plt.savefig("images/branch_sales.png", bbox_inches="tight")

# %%
payment_count = df["Payment"].value_counts()

payment_count

# %%
payment_count.plot(kind="pie", autopct="%1.1f%%")

plt.title("Payment Methods")
plt.ylabel("")
# plt.show()

plt.savefig("images/payment_methods.png", bbox_inches="tight")

# %%
gender_count = df["Gender"].value_counts()

gender_count

# %%
gender_count.plot(kind="bar")

plt.title("Customers by Gender")
plt.ylabel("Count")
# plt.show()

plt.savefig("images/gender_count.png", bbox_inches="tight")

# %%
city_sales = (
    df.groupby("City")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

city_sales

# %%
city_sales.plot(kind="bar")

plt.title("Sales by City")
plt.ylabel("Total Sales")
# plt.show()

plt.savefig("images/sales_by_city.png", bbox_inches="tight")

# %% [markdown]
# # Findings
# 
# 1. Food and beverages category generated the highest sales.
# 2. Branch Giza achieved the highest revenue.
# 3. E-wallet was the most popular payment method.
# 4. Female customers slightly outnumbered male customers.
# 5. Naypyitaw generated the highest total sales.


