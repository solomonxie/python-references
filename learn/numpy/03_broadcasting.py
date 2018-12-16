"""
Broadcasting lets NumPy apply operations across arrays of different shapes
without explicit loops or copies.
"""
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])
print(f"a + b (row broadcast):\n{a + b}")

col = np.array([[1], [2]])
print(f"a + col (column broadcast):\n{a + col}")

scaled = a * 2
print(f"a * 2:\n{scaled}")

normalized = (a - a.mean()) / a.std()
print(f"Normalized:\n{normalized}")
