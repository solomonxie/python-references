"""
Split-apply-combine with groupby: aggregating values per group.
"""
import pandas as pd

df = pd.DataFrame({
    "city": ["NYC", "LA", "NYC", "SF", "LA"],
    "sales": [100, 150, 200, 120, 90],
    "quarter": ["Q1", "Q1", "Q2", "Q1", "Q2"],
})

print(f"Sum by city:\n{df.groupby('city')['sales'].sum()}")
print(f"Mean by city+quarter:\n{df.groupby(['city', 'quarter'])['sales'].mean()}")
print(f"Multiple aggs:\n{df.groupby('city')['sales'].agg(['sum', 'mean', 'count'])}")
