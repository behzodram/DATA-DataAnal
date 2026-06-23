# 🛒 Supermarket Sales Analysis

Exploratory Data Analysis (EDA) of a supermarket chain with 3 branches across Myanmar (Yangon, Mandalay, Naypyitaw). Dataset contains 1,000 transactions from January–March 2019.

---

## 📁 Project Structure

```
DataAnal/
├── data/
│   └── SuperMarket.csv
├── images/
│   ├── sales_by_product.png
│   ├── branch_sales.png
│   ├── payment_methods.png
│   ├── gender_count.png
│   ├── sales_by_city.png
│   ├── sales_by_hour.png
│   └── correlation_heatmap.png
├── analysis.ipynb
├── requirements.txt
└── README.md
```

---

## 🛠️ Tools & Libraries

| Tool              | Purpose               |
|-------------------|-----------------------|
| Python 3.13.1     | Core language         |
| Pandas            | Data manipulation     |
| Matplotlib        | Visualization         |
| Seaborn           | Advanced visualization|
| Jupyter Notebook  | Interactive analysis  |

---

## ❓ Questions Explored

1. Which product line generated the highest sales?
2. Which branch performed best?
3. What payment methods are most popular?
4. How are customers distributed by gender?
5. Which city had the highest total sales?
6. At what hour of day are sales highest?
7. How do numeric variables correlate with each other?

---

## 📊 Key Findings

1. **Food and Beverages** generated the highest total sales among all product lines.
2. **Branch A (Yangon)** achieved the highest revenue across all branches.
3. **E-wallet** was the most popular payment method (~34.5%).
4. Female customers slightly outnumbered male customers (501 vs 499).
5. **Naypyitaw** recorded the highest total city sales.
6. Peak shopping hours were around **7 PM**.

---

## 🚀 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/behzodram/DATA-DataAnal.git
cd DATA-DataAnal

# 2. Install dependencies
pip install -r requirements.txt

# 3. Open notebook
jupyter notebook analysis.ipynb
```

---

## 📂 Dataset

- **Source:** [Kaggle — Supermarket Sales](https://www.kaggle.com/datasets/faresashraf1001/supermarket-sales)
- **Size:** 1,000 rows × 17 columns
- **Period:** January 2019 – March 2019