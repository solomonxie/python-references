"""
Handling missing data: detecting, dropping, and filling NaN values.
"""
import numpy as np
import pandas as pd

df = pd.DataFrame({
    "a": [1, np.nan, 3, None],
    "b": [np.nan, 2, 3, 4],
})

print(f"DataFrame:\n{df}")
print(f"Null mask:\n{df.isna()}")
print(f"Drop rows with any NaN:\n{df.dropna()}")
print(f"Fill with 0:\n{df.fillna(0)}")
print(f"Forward-fill:\n{df.ffill()}")
