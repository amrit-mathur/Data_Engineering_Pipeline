import pandas as pd
import mysql.connector
from pathlib import Path
import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)


GOLD = Path(config["paths"]["gold"])

conn = mysql.connector.connect(
    host=config["db"]["host"],
    user=config["db"]["user"],
    password=config["db"]["password"],
    database=config["db"]["database"]
)
cursor = conn.cursor()
category_df = pd.read_csv(GOLD / "category_summary.csv")
top_df = pd.read_csv(GOLD / "top_products.csv")

for _, row in category_df.iterrows():
    cursor.execute(
        "INSERT INTO gold_category_summary VALUES (%s, %s, %s)",
        (row["category"], row["total_quantity"], row["avg_price"])
    )

for _, row in top_df.iterrows():
    cursor.execute(
        "INSERT INTO gold_top_products VALUES (%s, %s, %s)",
        (row["product_id"], row["title"], row["total_quantity"])
    )
conn.commit()
cursor.close()
conn.close()