# $ python learn/dataframe/10_io_csv.py
# + to_csv/read_csv round trip.
# Step 10: persist the frame to disk and reload it.

import os
import tempfile

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

    with tempfile.TemporaryDirectory() as tmp:      # Step 10: own scratch dir, cleaned up on exit
        path = os.path.join(tmp, "employees.csv")
        df.to_csv(path, index=False)                # Step 10: write to CSV
        reloaded = pd.read_csv(path)                # Step 10: read back
        print(reloaded)
        print(reloaded.dtypes)                      # Step 10: NaN roundtrips, but dtypes can shift (e.g. int -> float)
