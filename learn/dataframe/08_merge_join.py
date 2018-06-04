# $ python learn/dataframe/08_merge_join.py
# + merge() to join another table, and concat() to stack more rows.
# Step 8: bring in data from a second DataFrame.

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

    depts = pd.DataFrame({                                     # Step 8: a second, smaller table
        "dept": ["eng", "sales", "hr"],
        "location": ["Seattle", "NYC", "NYC"],
    })
    merged = df.merge(depts, on="dept", how="left")            # Step 8: left join keeps every row of df
    print(merged)

    more_hires = pd.DataFrame({                                # Step 8: same columns as df, new rows
        "name": ["Frank"], "dept": ["hr"], "age": [33], "salary": [65000],
        "bonus": [6500.0], "level": ["senior"], "manager": ["Han"],
    })
    print(pd.concat([df, more_hires], ignore_index=True))      # Step 8: stack rows, renumber the index
