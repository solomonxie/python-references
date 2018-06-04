# $ python learn/dataframe/02_selection.py
# + column selection and loc/iloc row selection.
# Step 2: pick columns and rows out of the DataFrame.

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

    print(df["name"])                       # Step 2: single column -> Series
    print(df[["name", "salary"]])            # Step 2: multiple columns -> DataFrame
    print(df.loc[0:2, ["name", "dept"]])     # Step 2: label-based selection, end label is inclusive
    print(df.iloc[0:2, 0:2])                 # Step 2: position-based selection, end index is exclusive
