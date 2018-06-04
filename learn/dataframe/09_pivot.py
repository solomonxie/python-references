# $ python learn/dataframe/09_pivot.py
# + pivot_table() to reshape long data wide, and melt() to go back.
# Step 9: reshape the frame instead of joining another one.

import numpy as np
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
    df["manager"] = ["Zoe", None, "Zoe", np.nan, "Han"]

    pivot = df.pivot_table(values="salary", index="dept", columns="level", aggfunc="mean")  # Step 9: long -> wide
    print(pivot)

    long = df.melt(                                             # Step 9: wide -> long, the inverse of pivot_table
        id_vars=["name"], value_vars=["age", "salary"],
        var_name="metric", value_name="value",
    )
    print(long)
