# Task 7: Basic Sales Summary from a Tiny SQLite Database

## Project Overview
This project was completed as part of my Data Analyst Internship - Task 7. The objective is to use SQL inside Python to calculate total quantity sold and total revenue, print the results, and create a simple bar chart.

## Tools
- Python
- SQLite / sqlite3
- Pandas
- Matplotlib
- Jupyter Notebook

## Dataset
A small SQLite database named `sales_data.db` was created with one `sales` table.

Columns:
- `id`
- `product`
- `quantity`
- `price`

## SQL Analysis
The project uses SQL aggregation functions:
- `SUM(quantity)` for total quantity sold
- `SUM(quantity * price)` for revenue
- `GROUP BY product` for product-wise summary
- `ORDER BY revenue DESC` for sorting

## Visualization
A basic Matplotlib bar chart compares revenue by product.

## Project Files
- `sales_data.db` - SQLite database
- `Task_7_Sales_Summary.py` - Python script
- `Task_7_Sales_Summary.ipynb` - Jupyter Notebook
- `sales_chart.png` - Revenue bar chart
- `README.md` - Project documentation

## Conclusion
This project demonstrates how Python can connect to a SQLite database, run SQL queries, summarize sales data with Pandas, and visualize the result using Matplotlib.
