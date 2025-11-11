import pandas as pd
import mysql.connector
import requests
import io

# MySQL Connection
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",  # Change to your MySQL username
    password="root1824",  # Change to your MySQL password
    database="Northwind"
)
cursor = conn.cursor()

# GitHub Raw File Links
github_files = {
    "Customers": "https://raw.githubusercontent.com/MontyVasita18/Sales-Data-Analysis-Using-Python-SQL/main/Customers.csv",
    "Employees": "https://raw.githubusercontent.com/MontyVasita18/Sales-Data-Analysis-Using-Python-SQL/main/Employees.csv",
    "Orders": "https://raw.githubusercontent.com/MontyVasita18/Sales-Data-Analysis-Using-Python-SQL/main/Orders%20(1).csv",
    "Products": "https://raw.githubusercontent.com/MontyVasita18/Sales-Data-Analysis-Using-Python-SQL/main/Products.csv",
    "Suppliers": "https://raw.githubusercontent.com/MontyVasita18/Sales-Data-Analysis-Using-Python-SQL/main/Suppliers.csv"
}

# Insert data into MySQL
for table, url in github_files.items():
    try:
        print(f"Fetching {table} data from GitHub...")
        response = requests.get(url)
        response.raise_for_status()
        df = pd.read_csv(io.StringIO(response.text))

        # Trim whitespace from column names
        df.columns = df.columns.str.strip()
        print(f"Columns in {table}: {df.columns.tolist()}")  # Debug print

        # Replace NaN values with None for SQL compatibility
        df = df.where(pd.notna(df), None)

        # Ensure column names match database schema
        column_mapping = {
            "_Sales": "Sales",  # Example: rename _Sales if it doesn't exist in DB
            "Full Name": "FullName"  # Rename to match DB column name
        }
        df.rename(columns=column_mapping, inplace=True)

        # Check for rows with NaN values
        if df.isnull().values.any():
            print(f"DataFrame with NaN values in {table}:")
            print(df[df.isnull().any(axis=1)])  # Print rows with NaN values

        # Handle Date Format (Convert to 'YYYY-MM-DD')
        for col in df.columns:
            if "date" in col.lower():
                df[col] = pd.to_datetime(df[col], errors='coerce', dayfirst=True).dt.strftime('%Y-%m-%d')

        # Prepare Insert Statement with ON DUPLICATE KEY UPDATE
        cols = ', '.join([f"`{col}`" for col in df.columns])
        sql = f"INSERT INTO `{table}` ({cols}) VALUES ({', '.join(['%s'] * len(df.columns))}) "
        sql += "ON DUPLICATE KEY UPDATE " + ', '.join([f"`{col}`=VALUES(`{col}`)" for col in df.columns])

        # Insert data in batches, filtering out any rows with NaN
        valid_rows = df.dropna()
        if not valid_rows.empty:
            cursor.executemany(sql, valid_rows.values.tolist())
            conn.commit()
            print(f"{table} data inserted successfully.")
        else:
            print(f"No valid data to insert for {table}.")

    except mysql.connector.Error as db_error:
        print(f"Database error in {table}: {db_error}")
    except requests.HTTPError as http_error:
        print(f"HTTP error fetching {table}: {http_error}")
    except Exception as e:
        print(f"Error in {table}: {e}")

# Close MySQL connection
cursor.close()
conn.close()
print("All tables processed successfully.")