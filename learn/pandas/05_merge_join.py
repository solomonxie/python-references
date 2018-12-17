"""
Combining DataFrames with merge (SQL-style joins) and concat.
"""
import pandas as pd

users = pd.DataFrame({"user_id": [1, 2, 3], "name": ["Alice", "Bob", "Carol"]})
orders = pd.DataFrame({"user_id": [1, 1, 2], "amount": [50, 30, 75]})

print(f"Inner join:\n{pd.merge(users, orders, on='user_id', how='inner')}")
print(f"Left join:\n{pd.merge(users, orders, on='user_id', how='left')}")

more_users = pd.DataFrame({"user_id": [4], "name": ["Dave"]})
print(f"Concat:\n{pd.concat([users, more_users], ignore_index=True)}")
