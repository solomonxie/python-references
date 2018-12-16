"""
Aggregate functions: sum, mean, min/max, and axis-wise reductions.
"""
import numpy as np

a = np.arange(1, 13).reshape(3, 4)
print(f"Array:\n{a}")
print(f"Sum: {a.sum()}, Mean: {a.mean()}")
print(f"Column sums: {a.sum(axis=0)}")
print(f"Row means: {a.mean(axis=1)}")
print(f"Min: {a.min()}, Max: {a.max()}, Argmax: {a.argmax()}")
print(f"Cumulative sum: {a.cumsum()}")
