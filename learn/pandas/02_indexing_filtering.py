"""
Selecting and filtering rows/columns with loc, iloc, and boolean conditions.
"""
import pandas as pd

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
