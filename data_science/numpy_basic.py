"""
NumPy basics: array creation, indexing/slicing, broadcasting, aggregations,
and linear algebra.
"""
import numpy as np


def array_creation():
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


def indexing_slicing():
    a = np.arange(20).reshape(4, 5)
    print(f"Array:\n{a}")
    print(f"Row 1: {a[1]}")
    print(f"Column 2: {a[:, 2]}")
    print(f"Sub-block:\n{a[1:3, 2:4]}")

    mask = a % 3 == 0
    print(f"Divisible by 3: {a[mask]}")

    idx = [0, 2]
    print(f"Fancy-indexed rows:\n{a[idx]}")


def broadcasting():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([10, 20, 30])
    print(f"a + b (row broadcast):\n{a + b}")

    col = np.array([[1], [2]])
    print(f"a + col (column broadcast):\n{a + col}")

    scaled = a * 2
    print(f"a * 2:\n{scaled}")

    normalized = (a - a.mean()) / a.std()
    print(f"Normalized:\n{normalized}")


def aggregations():
    a = np.arange(1, 13).reshape(3, 4)
    print(f"Array:\n{a}")
    print(f"Sum: {a.sum()}, Mean: {a.mean()}")
    print(f"Column sums: {a.sum(axis=0)}")
    print(f"Row means: {a.mean(axis=1)}")
    print(f"Min: {a.min()}, Max: {a.max()}, Argmax: {a.argmax()}")
    print(f"Cumulative sum: {a.cumsum()}")


def linear_algebra():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])

    print(f"Dot product:\n{a.dot(b)}")
    print(f"Matrix multiply (@):\n{a @ b}")
    print(f"Transpose:\n{a.T}")
    print(f"Determinant: {np.linalg.det(a):.2f}")
    print(f"Inverse:\n{np.linalg.inv(a)}")

    eigvals, eigvecs = np.linalg.eig(a)
    print(f"Eigenvalues: {eigvals}")


if __name__ == "__main__":
    for demo in (array_creation, indexing_slicing, broadcasting, aggregations, linear_algebra):
        print(f"--- {demo.__name__} ---")
        demo()
