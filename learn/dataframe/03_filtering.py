# $ python learn/dataframe/03_filtering.py
# + boolean-mask filtering and the equivalent query() syntax.
# Step 3: keep only the rows matching a condition.

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

    print(df["name"])
    print(df[["name", "salary"]])
    print(df.loc[0:2, ["name", "dept"]])
    print(df.iloc[0:2, 0:2])

    engineers = df[df["dept"] == "eng"]                          # Step 3: boolean mask
    senior_eng = df[(df["dept"] == "eng") & (df["age"] > 28)]    # Step 3: combine masks with & (parens required)
    via_query = df.query("dept == 'eng' and age > 28")           # Step 3: same filter, query() syntax
    print(engineers)
    print(senior_eng)
    print(via_query)
