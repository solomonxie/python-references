# $ python learn/dataframe/06_groupby.py
# + groupby with a single aggregation and with agg() for several at once.
# Step 6: summarize rows per group instead of sorting/filtering them.

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

    print(df.groupby("dept")["salary"].mean())      # Step 6: one aggregation per group

    print(df.groupby("dept").agg(                    # Step 6: multiple named aggregations at once
        avg_salary=("salary", "mean"),
        headcount=("name", "count"),
    ))
