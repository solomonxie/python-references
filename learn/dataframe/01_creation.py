# $ python learn/dataframe/01_creation.py
# Build a DataFrame from a dict of columns; inspect its shape/dtypes/head.
# Step 1: create a DataFrame and look at its basic structure.

import pandas as pd


def build_employees() -> pd.DataFrame:
    return pd.DataFrame({
        "name": ["Alice", "Bob", "Carol", "Dave", "Eve"],
        "dept": ["eng", "eng", "sales", "sales", "eng"],
        "age": [30, 25, 35, 40, 28],
        "salary": [95000, 80000, 70000, 72000, 99000],
    })


if __name__ == "__main__":
    df = build_employees()
    print(df)
    print(f"shape: {df.shape}")
    print(f"dtypes:\n{df.dtypes}")
    print(f"head(2):\n{df.head(2)}")
