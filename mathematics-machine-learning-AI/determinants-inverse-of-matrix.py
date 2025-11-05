# DETERMINANTS - yếu tố quyết định
# Is a single number that provides info about a square matrix
# If determinant = 0, the matrix is singular - no inverse (nghịch đảo) exists
# If determinant != 0, the matrix is invertible (có thể đảo ngược) (you can compute its inverse)
# Geometrically (Về mặt hình học), it represents area, volume, or scale change
# Formula for 2x2 matrix: det ([a b], [c, d]) = ad = bc

import numpy as np

A = np.array([[2, 3], [1, 4]])
determinant = np.linalg.det(A)
print("Determinant of array A is \n", determinant)

# INVERSE - nghịch đảo
# Only square matrices with a non-zero determinant have an inverse.
# The inverse of matrix A is another matrix A⁻¹ such that: A * A⁻¹ = I where I is the identity matrix

inverse = np.linalg.inv(A)
print("Inverse of array A \n", inverse)

# EIGENVALUES & EIGENVECTORS
# When multiplying a matrix A by a vector v, usually the result changes direction. But sometimes, it only streches or shrinks, not rotate
# Those special vectors are called eigenvectors, and the amount they are scaled by are the eigenvalues
# The equation: A * v = λ * v
# A - a square matrix
# v - the eigenvector - A direction that remains unchanged (except scaled) when multiplied by a matrix
# λ - the eigenvalue - The factor by which the eigenvector is scaled
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues \n", eigenvalues)
print("Eigenvectors \n", eigenvectors)