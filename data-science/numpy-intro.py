import numpy as np

arr = np.array([1, 2, 3, 4])
print("A numpy array", arr)

zeros = np.zeros((3, 3))
print("A metric of 3 by 3 zeros with zeros function", zeros)

ones = np.ones((2, 4))
print("A metric of 2 by 4 arrays of 1 with ones function", ones)

range_array = np.arange(1, 10, 2)
print("An array between 1 and 10 with spacing of 2")

linspace_array = np.linspace(0, 1, 5)
print("An array of 5 numbers between 0 and 1")
