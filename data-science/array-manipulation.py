import numpy as np

array = np.array([1, 2, 3, 4, 5, 6])
reshaped_array = array.reshape((2, 3))
print("Reshape the array to an array with 2 arrays with 3 numbers each", reshaped_array)

expanded_array = array[:, np.newaxis]
print("Add dimention to the array by adding new axis", expanded_array)

array2 = np.array([1, 2, 3, 4, 5, 6])
print("Adding 2 arrays together", array + array2)
print("Multiplying 2 arrays togehter", array * array2)
print("Dividing 2 arrays", array/array2)

array3 = np.array([4, 16, 25])
print("Square root of array", np.sqrt(array3))
print("Sum of array", np.sum(array3))
print("Mean of array", np.mean(array3))
print("Max of the array", np.max(array3))