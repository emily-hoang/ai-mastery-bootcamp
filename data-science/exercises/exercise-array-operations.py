import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original matrix: \n", matrix)

transpose = matrix.T
print("Transposed matrix: \n", transpose)

matrix1 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("Multiplying 2 matrixes together", matrix * matrix1)
