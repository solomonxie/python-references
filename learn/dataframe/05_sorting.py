# $ python learn/dataframe/05_sorting.py
# + sort_values (single/multiple keys) and sort_index.
# Step 5: reorder rows instead of filtering them.

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
    df["bonus"] = df["salary"] * 0.1
    df["level"] = df["age"].apply(lambda a: "senior" if a >= 30 else "junior")

    print(df.sort_values("salary", ascending=False))    # Step 5: sort by one column
    print(df.sort_values(["dept", "age"]))               # Step 5: sort by multiple columns, left to right
    print(df.sort_index())                               # Step 5: sort by the row index
