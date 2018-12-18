"""
pandas basics: Series/DataFrame, indexing/filtering, groupby, missing data,
and merge/join.
"""
import numpy as np
import pandas as pd


def series_dataframe():
    s = pd.Series([10, 20, 30], index=["a", "b", "c"])
    print(f"Series:\n{s}")

    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Carol"],
        "age": [30, 25, 35],
        "city": ["NYC", "LA", "SF"],
    })
    print(f"DataFrame:\n{df}")
    print(f"Shape: {df.shape}, Columns: {list(df.columns)}")
    print(f"dtypes:\n{df.dtypes}")


def indexing_filtering():
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Carol", "Dave"],
        "age": [30, 25, 35, 40],
        "city": ["NYC", "LA", "SF", "NYC"],
    })

    print(f"By label (loc):\n{df.loc[0:1, ['name', 'age']]}")
    print(f"By position (iloc):\n{df.iloc[1:3, :2]}")
    print(f"Age > 30:\n{df[df['age'] > 30]}")
    print(f"City == NYC:\n{df[df['city'] == 'NYC']}")
    print(f"Combined filter:\n{df[(df['age'] > 25) & (df['city'] == 'NYC')]}")


def groupby_aggregation():
    df = pd.DataFrame({
        "city": ["NYC", "LA", "NYC", "SF", "LA"],
        "sales": [100, 150, 200, 120, 90],
        "quarter": ["Q1", "Q1", "Q2", "Q1", "Q2"],
    })

    print(f"Sum by city:\n{df.groupby('city')['sales'].sum()}")
    print(f"Mean by city+quarter:\n{df.groupby(['city', 'quarter'])['sales'].mean()}")
    print(f"Multiple aggs:\n{df.groupby('city')['sales'].agg(['sum', 'mean', 'count'])}")


def missing_data():
    df = pd.DataFrame({
        "a": [1, np.nan, 3, None],
        "b": [np.nan, 2, 3, 4],
    })

    print(f"DataFrame:\n{df}")
    print(f"Null mask:\n{df.isna()}")
    print(f"Drop rows with any NaN:\n{df.dropna()}")
    print(f"Fill with 0:\n{df.fillna(0)}")
    print(f"Forward-fill:\n{df.ffill()}")


def merge_join():
    users = pd.DataFrame({"user_id": [1, 2, 3], "name": ["Alice", "Bob", "Carol"]})
    orders = pd.DataFrame({"user_id": [1, 1, 2], "amount": [50, 30, 75]})

    print(f"Inner join:\n{pd.merge(users, orders, on='user_id', how='inner')}")
    print(f"Left join:\n{pd.merge(users, orders, on='user_id', how='left')}")

    more_users = pd.DataFrame({"user_id": [4], "name": ["Dave"]})
    print(f"Concat:\n{pd.concat([users, more_users], ignore_index=True)}")


if __name__ == "__main__":
    for demo in (series_dataframe, indexing_filtering, groupby_aggregation, missing_data, merge_join):
        print(f"--- {demo.__name__} ---")
        demo()
