import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="AMRIT",
    database="ecommerce"
)
df = pd.read_sql("SELECT * FROM products", conn)
print(df)

ds = pd.read_sql("SELECT * FROM users", conn)
print(ds)