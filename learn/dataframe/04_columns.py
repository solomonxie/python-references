# $ python learn/dataframe/04_columns.py
# + adding a computed column, apply() per element, and drop() for a column-less copy.
# Step 4: derive new columns from existing ones.

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

    engineers = df[df["dept"] == "eng"]
    senior_eng = df[(df["dept"] == "eng") & (df["age"] > 28)]
    via_query = df.query("dept == 'eng' and age > 28")
    print(engineers)
    print(senior_eng)
    print(via_query)

    df["bonus"] = df["salary"] * 0.1                                            # Step 4: vectorized new column
    df["level"] = df["age"].apply(lambda a: "senior" if a >= 30 else "junior")  # Step 4: apply() per element
    without_bonus = df.drop(columns=["bonus"])                                  # Step 4: drop() returns a new frame
    print(df)
    print(without_bonus)
