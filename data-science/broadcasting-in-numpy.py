import numpy as np
# Broadcasting allows NumPy to treat arrays with different shapes during arithmetic operations. 
# Subject to certain constraints, the smaller array is “broadcast” across the larger array so that they have compatible shapes.\
  
# Array and scalar broadcasting
arr = np.array([1, 2, 3])
print("Expanded array by plus 10", arr + 10)

matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([1, 0, 1])
print("Adding array 1 with array 2", matrix + vector)

print("Sum of all elements in the array: ", np.sum(arr))
print("Mean (average value) of the array: ", np.mean(arr))
print("Min of the array: ", np.min(arr))
print("Max of the array: ", np.max(arr))
print("Standard deviation is a measure that is used to quantify the amount of variation or dispersion a set of data points has from the average (mean) of the data. In simpler terms, it shows how much the data varies from the mean. ", np.sum(arr, axis=0))
print("A low standard deviation indicates that the data points tend to be close to the mean.")
print("A high standard deviation indicates that the data points are spread out over a larger range of values.")
print("sum along colums: ", np.sum(arr, axis=0))