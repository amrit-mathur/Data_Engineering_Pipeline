import json
import pandas as pd
from pathlib import Path
import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)
BRONZE = Path(config["paths"]["bronze"])
SILVER = Path(config["paths"]["silver"])
(SILVER / "products").mkdir(parents=True, exist_ok=True)
(SILVER / "users").mkdir(parents=True, exist_ok=True)
(SILVER / "carts").mkdir(parents=True, exist_ok=True)

product_file = list((BRONZE / "products").glob("*.json"))[-1]
with open(product_file, "r") as f:
    products = json.load(f)
df_products = pd.DataFrame(products)
df_products = df_products.rename(columns={"id": "product_id"})
df_products = df_products[["product_id", "title", "price", "category", "batch_id"]]
df_products = df_products.dropna()
df_products = df_products.drop_duplicates()
df_products.to_csv(SILVER / "products" / "products.csv", index=False)

user_file = list((BRONZE / "users").glob("*.json"))[-1]
with open(user_file, "r") as f:
    users = json.load(f)
df_users = pd.DataFrame(users)
df_users["city"] = df_users["address"].apply(lambda x: x["city"])
df_users = df_users.rename(columns={"id": "user_id"})
df_users = df_users[["user_id", "email", "username", "city", "batch_id"]]
df_users = df_users.dropna()
df_users = df_users.drop_duplicates()
df_users.to_csv(SILVER / "users" / "users.csv", index=False)

cart_file = list((BRONZE / "carts").glob("*.json"))[-1]
with open(cart_file, "r") as f:
    carts = json.load(f)
df_carts = pd.DataFrame(carts)
df_carts = df_carts.rename(columns={"id": "cart_id"})
df_carts[["cart_id", "userId", "date", "batch_id"]].to_csv(
    SILVER / "carts" / "carts.csv", index=False
)
rows = []
for _, row in df_carts.iterrows():
    for item in row["products"]:
        rows.append({
            "cart_id": row["cart_id"],
            "product_id": item["productId"],
            "quantity": item["quantity"],
            "batch_id": row["batch_id"]
        })
df_items = pd.DataFrame(rows)
df_items = df_items.dropna()
df_items = df_items.drop_duplicates()
df_items.to_csv(SILVER / "carts" / "cart_items.csv", index=False)