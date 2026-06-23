# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Grafik uslubi
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 5)

# %%
# ============================================================
# 1. DATASETNI YUKLASH
# ============================================================
df = pd.read_csv("data/SuperMarket.csv")

print("Shape:", df.shape)
df.head()

# %%
# ============================================================
# 2. UMUMIY MA'LUMOT
# ============================================================
df.info()

# %%
df.describe()

# %%
# ============================================================
# 3. NULL QIYMATLARNI TEKSHIRISH
# ============================================================
print("Null qiymatlar:")
print(df.isnull().sum())

# %%
# ============================================================
# 4. MAHSULOT LINIYASI BO'YICHA SOTUV
# ============================================================
sales_by_product = (
    df.groupby("Product line")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots()
bars = ax.bar(sales_by_product.index, sales_by_product.values, color=sns.color_palette("Blues_d", len(sales_by_product)))
ax.set_title("Sales by Product Line", fontsize=14, fontweight="bold")
ax.set_ylabel("Total Sales")
ax.set_xlabel("Product Line")
plt.xticks(rotation=30, ha="right")

# Har bir ustun ustiga qiymat yoz
for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 500,
            f"${bar.get_height():,.0f}", ha="center", va="bottom", fontsize=9)

plt.tight_layout()
plt.savefig("images/sales_by_product.png", bbox_inches="tight")
plt.show()

# Tahlil
top_product = sales_by_product.index[0]
print(f"\n✅ Eng ko'p sotuv: {top_product} — ${sales_by_product.iloc[0]:,.2f}")

# %%
# ============================================================
# 5. FILIAL BO'YICHA SOTUV
# ============================================================
branch_sales = (
    df.groupby("Branch")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots()
bars = ax.bar(branch_sales.index, branch_sales.values, color=sns.color_palette("Greens_d", len(branch_sales)))
ax.set_title("Sales by Branch", fontsize=14, fontweight="bold")
ax.set_ylabel("Total Sales")
ax.set_xlabel("Branch")

for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 300,
            f"${bar.get_height():,.0f}", ha="center", va="bottom", fontsize=9)

plt.tight_layout()
plt.savefig("images/branch_sales.png", bbox_inches="tight")
plt.show()

top_branch = branch_sales.index[0]
print(f"\n✅ Eng yuqori daromadli filial: Branch {top_branch} — ${branch_sales.iloc[0]:,.2f}")

# %%
# ============================================================
# 6. TO'LOV USULLARI
# ============================================================
payment_count = df["Payment"].value_counts()

fig, ax = plt.subplots()
ax.pie(payment_count.values,
       labels=payment_count.index,
       autopct="%1.1f%%",
       colors=sns.color_palette("Set2"),
       startangle=90)
ax.set_title("Payment Methods", fontsize=14, fontweight="bold")

plt.tight_layout()
plt.savefig("images/payment_methods.png", bbox_inches="tight")
plt.show()

top_payment = payment_count.index[0]
print(f"\n✅ Eng mashhur to'lov usuli: {top_payment} ({payment_count.iloc[0]} ta mijoz)")

# %%
# ============================================================
# 7. JINS BO'YICHA MIJOZLAR
# ============================================================
gender_count = df["Gender"].value_counts()

fig, ax = plt.subplots()
bars = ax.bar(gender_count.index, gender_count.values,
              color=["#4C72B0", "#DD8452"], width=0.4)
ax.set_title("Customers by Gender", fontsize=14, fontweight="bold")
ax.set_ylabel("Count")
ax.set_xlabel("Gender")

for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
            str(int(bar.get_height())), ha="center", va="bottom", fontsize=10)

plt.tight_layout()
plt.savefig("images/gender_count.png", bbox_inches="tight")
plt.show()

print(f"\n✅ Ayollar: {gender_count.get('Female', 0)} | Erkaklar: {gender_count.get('Male', 0)}")

# %%
# ============================================================
# 8. SHAHAR BO'YICHA SOTUV
# ============================================================
city_sales = (
    df.groupby("City")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots()
bars = ax.bar(city_sales.index, city_sales.values,
              color=sns.color_palette("Oranges_d", len(city_sales)))
ax.set_title("Sales by City", fontsize=14, fontweight="bold")
ax.set_ylabel("Total Sales")
ax.set_xlabel("City")

for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 300,
            f"${bar.get_height():,.0f}", ha="center", va="bottom", fontsize=9)

plt.tight_layout()
plt.savefig("images/sales_by_city.png", bbox_inches="tight")
plt.show()

top_city = city_sales.index[0]
print(f"\n✅ Eng ko'p sotuv shahri: {top_city} — ${city_sales.iloc[0]:,.2f}")

# %%
# ============================================================
# 9. KORRELYATSIYA HEATMAP
# ============================================================
numeric_cols = df.select_dtypes(include="number")

fig, ax = plt.subplots(figsize=(10, 7))
sns.heatmap(numeric_cols.corr(), annot=True, fmt=".2f",
            cmap="coolwarm", ax=ax, linewidths=0.5)
ax.set_title("Correlation Heatmap", fontsize=14, fontweight="bold")

plt.tight_layout()
plt.savefig("images/correlation_heatmap.png", bbox_inches="tight")
plt.show()

# %%
# ============================================================
# 10. SOAT BO'YICHA SOTUV (Qaysi vaqt gavjum?)
# ============================================================
df["Hour"] = pd.to_datetime(df["Time"]).dt.hour
hourly_sales = df.groupby("Hour")["Sales"].sum()

fig, ax = plt.subplots()
ax.plot(hourly_sales.index, hourly_sales.values, marker="o", color="#2196F3", linewidth=2)
ax.set_title("Sales by Hour of Day", fontsize=14, fontweight="bold")
ax.set_xlabel("Hour")
ax.set_ylabel("Total Sales")
ax.set_xticks(hourly_sales.index)

plt.tight_layout()
plt.savefig("images/sales_by_hour.png", bbox_inches="tight")
plt.show()

peak_hour = hourly_sales.idxmax()
print(f"\n✅ Eng gavjum soat: {peak_hour}:00")

# %%
# ============================================================
# 11. XULOSALAR (Datadan olingan haqiqiy natijalar)
# ============================================================
print("=" * 50)
print("📊 XULOSALAR")
print("=" * 50)
print(f"1. Eng ko'p sotiladigan mahsulot: {top_product}")
print(f"2. Eng yuqori daromadli filial: Branch {top_branch}")
print(f"3. Eng mashhur to'lov usuli: {top_payment}")
print(f"4. Mijozlar jinsi: Ayollar {gender_count.get('Female',0)}, Erkaklar {gender_count.get('Male',0)}")
print(f"5. Eng ko'p sotuv shahri: {top_city}")
print(f"6. Savdo cho'qqisi soati: {peak_hour}:00")
print("=" * 50)