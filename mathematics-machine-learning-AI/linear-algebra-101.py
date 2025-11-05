# Vector - a 1-dimensional array of numbers. It's like a list of values.
# Example: vector = numpy.array([1, 2, 3, 4, 5])
# Matrix - a 2-dimensional array of numbers, like a grid or spreadsheet.
# Example: matrix = numpy.array([[1, 2, 3], [4, 5, 6]])
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Adding A and B: \n", A + B)
print("Substracting A and B: \n", A - B)

# Scalar Multiplication
C = 2 * A
print("Scalar Multiplication of array A with 2: \n", C)

# Matrix Multiplication - The number of columns in A must equal the number of rows in B.
# Matrix multiplication is not element-by-element. It follows a specific rule:
# If you multiply a matrix A of shape (m × n) by a matrix B of shape (n × p), the result is a matrix C of shape (m × p).

# How it works
# C[0][0] = (1*5 + 2*7) = 19
# C[0][1] = (1*6 + 2*8) = 22
# C[1][0] = (3*5 + 4*7) = 43
# C[1][1] = (3*6 + 4*8) = 50
D = np.dot(A, B)
# or
E = A @ B
print("Matrix Multiplication using dot(): \n", D)
print("Matrix Multiplication using @: \n", E)

# Identity Matrix - a special square matrix where:
# - All diagonal elements are 1
# - All of-diagonal elemnents are 0

# Square Identity Matrix
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
I = np.eye(3)
print("A Square Identity Matrix \n", I)

# Non-square Identity Matrix
#  [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]]
G = np.eye(3, 4)
print("Non-Square Identity Matrix \n", G)

# Diagnol Matrix
#  [[1 0 0]
#  [0 2 0]
#  [0 0 3]]
K = np.diag([1, 2, 3])
print("Diangol Matrix \n", K)

# Zero Matrix
#  [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]
H = np.zeros((3, 4))
print("Zero Matrix \n", H)
