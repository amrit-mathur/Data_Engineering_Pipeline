import requests
import json
from datetime import datetime
from pathlib import Path
import yaml


with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

batch_id = datetime.now().strftime("%d-%m-%y")
print("Batch ID:", batch_id)
base_path = Path(config["paths"]["bronze"])

products = requests.get(config["api"]["products"]).json()
for item in products:
    item["batch_id"] = batch_id
product_path = base_path / config["files"]["products"]
product_path.mkdir(parents=True, exist_ok=True)
product_file = product_path / f"{batch_id}_products.json"

with open(product_file, "w") as f:
    json.dump(products, f, indent=4)
print("Products saved at:", product_file)

users = requests.get(config["api"]["users"]).json()
for item in users:
    item["batch_id"] = batch_id
user_path = base_path / config["files"]["users"]
user_path.mkdir(parents=True, exist_ok=True)
user_file = user_path / f"{batch_id}_users.json"
with open(user_file, "w") as f:
    json.dump(users, f, indent=4)
print("Users saved at:", user_file)

carts = requests.get(config["api"]["carts"]).json()
for item in carts:
    item["batch_id"] = batch_id
cart_path = base_path / config["files"]["carts"]
cart_path.mkdir(parents=True, exist_ok=True)
cart_file = cart_path / f"{batch_id}_carts.json"

with open(cart_file, "w") as f:
    json.dump(carts, f, indent=4)
print("Carts saved at:", cart_file)