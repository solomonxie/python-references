"""
Series and DataFrame: pandas' core 1D and 2D labeled data structures.
"""
import pandas as pd

s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(f"Series:\n{s}")

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Carol"],
    "age": [30, 25, 35],
    "city": ["NYC", "LA", "SF"],
})
print(f"DataFrame:\n{df}")
print(f"Shape: {df.shape}, Columns: {list(df.columns)}")
print(f"dtypes:\n{df.dtypes}")
