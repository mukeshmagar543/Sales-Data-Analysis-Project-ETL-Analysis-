# 📊 Northwind Sales Data Analysis Project (ETL + Analysis)

## 🗂 Project Overview
This project involves performing end-to-end **ETL (Extract, Transform, Load)** operations on the Northwind database and conducting insightful data analysis using SQL and Python (Pandas + Matplotlib/Seaborn).

## 🔄 ETL Workflow

### ✅ Extract
- Data is pulled from multiple normalized tables in the **Northwind** MySQL database:
  - `Customers`
  - `Orders`
  - `Employees`
  - `Products`
  - `Suppliers`

### ✅ Transform
- Data from multiple tables is **merged** using SQL JOINs and Pandas `.merge()` on common keys such as `CustomerID`, `EmployeeID`, `ProductID`, etc.
- Calculated fields like `FinalPrice = Quantity * UnitPrice * (1 - Discount)`.
- Aggregated metrics like:
  - Total Orders by Country
  - Most ordered products
  - Customers with more than 5 orders
- Cleaned and structured data ready for analysis.

### ✅ Load
- Final results are loaded into **Pandas DataFrames**.
- Data is visualized using **bar charts**, **pie charts**, and **line plots**.
- Optionally, results can be exported to CSV or Excel for reporting.

## 📌 Key Insights & SQL Queries Used
- **Top 5 Countries by Customer Count**
- **Top 5 Most Expensive Products**
- **Order Distribution by Country**
- **Most Ordered Product by Quantity**
- **Employees with Most Orders Processed**
- **Customers without Orders**
- **Customers with More than 5 Orders**
- **Final Order Details with Discount Calculations**

## 📊 Visualizations
- Pie chart for most expensive products.
- Bar chart for total orders by country.
- Line chart for monthly order trends (if time-series included).

## 💻 Tools & Technologies
- **SQL (MySQL Workbench)**
- **Python (Jupyter Notebook in VS Code)**
- **Pandas** for data manipulation
- **Matplotlib/Seaborn** for visualization

## 📁 Project Structure
```
project_folder/
├── analysis.ipynb         # Jupyter notebook with ETL and analysis code
├── README.md              # Project description
└── exports/               # (Optional) Exported charts and CSVs
```

## 📈 Outcome
This project demonstrates the ability to:
- Work with relational databases
- Perform SQL-based and Python-based transformations
- Merge, clean, and analyze data
- Derive business insights from raw data
- Visualize results effectively

---
> ✅ This project can be extended further by adding time series, KPIs dashboards (Power BI/Tableau), or deploying the analysis as a web app.

