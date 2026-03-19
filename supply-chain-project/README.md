# 📦 Supply Chain Inventory Analysis and Data Cleaning

## 📌 Project Overview

This project focuses on cleaning and analyzing a supply chain inventory dataset to identify inefficiencies in inventory management, shipping performance, and demand patterns.

The dataset initially contained missing values, duplicate records, and inconsistent data entries. Using Python in VS Code, the data was cleaned and transformed into an analysis-ready format, enabling meaningful insights and better decision-making.

---

## ❗ Business Problem

Organizations often struggle with:

- Poor inventory visibility
- Overstocking or stock shortages
- Inefficient shipping and delivery delays
- Inconsistent and unreliable data

These challenges make it difficult to optimize operations and meet customer demand effectively.

---

## 🎯 Project Objectives

- Clean and standardize a raw supply chain dataset
- Handle missing values and duplicate records
- Identify inventory inefficiencies (stock vs demand)
- Evaluate shipping performance across transport modes
- Generate actionable business insights

---

## ⚙️ Methodology

### 1. Data Cleaning

- Standardized column names
- Removed duplicate rows (~124 duplicates)
- Handled missing values using:
  - Median (numerical data)
  - Mode (categorical data)
- Fixed inconsistent categorical values (e.g., `ROad`, `air`, `Rail` → standardized)

---

### 2. Feature Engineering

- **Inventory Turnover Ratio**
  - Measures how quickly inventory is sold
- **Estimated Profit**
  - Revenue minus total costs

---

### 3. Data Analysis

#### 📊 Analysis 1: Inventory vs Demand

- Compared stock levels with number of products sold

👉 **Key Finding:**

- Sales are significantly higher than stock levels
- Indicates strong demand but potential risk of stock shortages

---

#### 🚚 Analysis 2: Shipping Performance

- Compared average shipping time across transportation modes

👉 **Key Finding:**

- Some transport modes take longer to deliver than others
- Highlights opportunities to optimize logistics

---

## 📊 Key Insights

- High sales relative to stock levels indicate **strong demand and possible understocking**
- Certain transportation modes contribute to **longer delivery times**
- Data inconsistencies initially hid important operational issues
- Proper data cleaning is essential for reliable analysis

---

## 💡 Business Recommendations

- Increase inventory for high-demand products
- Optimize transportation strategies to reduce delivery time
- Improve data collection and validation processes
- Use data-driven forecasting for better inventory planning

---

## 🛠️ Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- VS Code

---

supply-chain-project/
│
├── data/
│ ├── raw/
│ │ └── dirty_supply_chain_inventory_dataset.csv
│ └── processed/
│ └── cleaned_supply_chain_inventory_dataset.csv
│
├── notebooks/
│ ├── 01_data_exploration.ipynb
│ ├── 02_data_cleaning.ipynb
│ ├── 03_exploratory_data_analysis.ipynb
│ └── 04_insights_and_recommendations.ipynb
│
├── src/
│ ├── cleaning.py
│ ├── visualize.py
│ ├── config.py
│ └── utils.py
│
├── outputs/
│ └── figures/
│
├── main.py
├── requirements.txt
└── README.md

---

## ▶️ How to Run the Project

```bash
# 1. Create virtual environment
python -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run main script
python main.py
```
