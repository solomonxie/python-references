"""
NumPy arrays: creating them from lists, ranges, and built-in constructors.
"""
import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(f"From list: {a}, dtype={a.dtype}")

zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
print(f"Zeros:\n{zeros}")
print(f"Ones:\n{ones}")

r = np.arange(0, 10, 2)
lin = np.linspace(0, 1, 5)
print(f"arange: {r}")
print(f"linspace: {lin}")

identity = np.eye(3)
print(f"Identity:\n{identity}")
