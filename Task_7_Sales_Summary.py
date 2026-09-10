import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("sales_data.db")
print("SQLite database connected successfully!")

query = """
SELECT product,
       SUM(quantity) AS total_qty,
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC;
"""

df = pd.read_sql_query(query, conn)
print("\nSales Summary:")
print(df.to_string(index=False))

query2 = """
SELECT SUM(quantity) AS total_quantity_sold,
       SUM(quantity * price) AS total_revenue
FROM sales;
"""
totals = pd.read_sql_query(query2, conn)
print("\nOverall Sales:")
print(totals.to_string(index=False))

df.plot(kind="bar", x="product", y="revenue", legend=False, figsize=(9,5))
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (INR)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("sales_chart.png", dpi=160)
plt.show()

conn.close()
