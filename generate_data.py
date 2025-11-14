import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta
import os

fake = Faker()
os.makedirs("data", exist_ok=True)

# Users
users = []
for i in range(200):
    users.append({
        "user_id": i+1,
        "name": fake.name(),
        "email": fake.email(),
        "signup_date": fake.date_between(start_date='-2y', end_date='today').isoformat()
    })
pd.DataFrame(users).to_csv("data/users.csv", index=False)

# Products
products = []
for i in range(150):
    products.append({
        "product_id": i+1,
        "name": fake.word().title(),
        "price": round(random.uniform(5, 500), 2),
        "category": fake.word()
    })
pd.DataFrame(products).to_csv("data/products.csv", index=False)

# Orders
orders = []
for i in range(300):
    orders.append({
        "order_id": i+1,
        "user_id": random.randint(1, 200),
        "order_date": fake.date_between(start_date='-1y', end_date='today').isoformat()
    })
pd.DataFrame(orders).to_csv("data/orders.csv", index=False)

# Order Items
order_items = []
for i in range(800):
    order_items.append({
        "order_item_id": i+1,
        "order_id": random.randint(1, 300),
        "product_id": random.randint(1, 150),
        "quantity": random.randint(1, 5)
    })
pd.DataFrame(order_items).to_csv("data/order_items.csv", index=False)

# Reviews
reviews = []
for i in range(200):
    reviews.append({
        "review_id": i+1,
        "user_id": random.randint(1, 200),
        "product_id": random.randint(1, 150),
        "rating": random.randint(1, 5),
        "review_date": fake.date_between(start_date='-1y', end_date='today').isoformat()
    })
pd.DataFrame(reviews).to_csv("data/reviews.csv", index=False)

print("Synthetic data successfully generated in ./data/")