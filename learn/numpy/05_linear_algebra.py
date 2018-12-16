"""
Basic linear algebra: dot products, matrix multiplication, transpose, inverse.
"""
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(f"Dot product:\n{a.dot(b)}")
print(f"Matrix multiply (@):\n{a @ b}")
print(f"Transpose:\n{a.T}")
print(f"Determinant: {np.linalg.det(a):.2f}")
print(f"Inverse:\n{np.linalg.inv(a)}")

eigvals, eigvecs = np.linalg.eig(a)
print(f"Eigenvalues: {eigvals}")
