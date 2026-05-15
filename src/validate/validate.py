import pandas as pd
from pathlib import Path
import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

SILVER = Path(config["paths"]["silver"])

def validate(df, name):
    print(name)
    print("Null values:")
    print(df.isnull().sum())
    print("\nDuplicate rows:", df.duplicated().sum())
    print("\nShape:", df.shape)

df_products = pd.read_csv(SILVER / "products" / "products.csv")
validate(df_products, "PRODUCTS")

df_users = pd.read_csv(SILVER / "users" / "users.csv")
validate(df_users, "USERS")

df_items = pd.read_csv(SILVER / "carts" / "cart_items.csv")
validate(df_items, "CART ITEMS")