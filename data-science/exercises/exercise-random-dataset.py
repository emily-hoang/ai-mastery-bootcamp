import numpy as np

arr = np.random.randint(1, 51, size=(5, 5))
print("Original random int array: \n", arr)

arr[arr > 25] = 0
print("Modified array by replacing int > 25 with 0: \n", arr)

print("Standard Deviation: ", np.std(arr))