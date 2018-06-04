# $ python learn/dataframe/07_missing_data.py
# + isna/fillna/dropna for handling missing values.
# Step 7: introduce a column with gaps and clean it up.

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

    df["manager"] = ["Zoe", None, "Zoe", np.nan, "Han"]   # Step 7: both None and np.nan count as missing

    print(df.isna())                                       # Step 7: boolean mask of missing cells
    print(df["manager"].fillna("N/A"))                      # Step 7: fill missing with a default
    print(df.dropna(subset=["manager"]))                    # Step 7: drop rows missing a given column
