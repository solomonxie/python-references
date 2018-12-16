"""
Indexing and slicing NumPy arrays, including boolean masks and fancy indexing.
"""
import numpy as np

a = np.arange(20).reshape(4, 5)
print(f"Array:\n{a}")
print(f"Row 1: {a[1]}")
print(f"Column 2: {a[:, 2]}")
print(f"Sub-block:\n{a[1:3, 2:4]}")

mask = a % 3 == 0
print(f"Divisible by 3: {a[mask]}")

idx = [0, 2]
print(f"Fancy-indexed rows:\n{a[idx]}")
