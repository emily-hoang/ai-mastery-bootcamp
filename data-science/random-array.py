import numpy as np

# The seed() method is used to initilised the random number generator. 
# By default the random number generator used the current system time.
# If you use the same seed value twice, you'll get the same random numbers.
np.random.seed(42)
random_array = np.random.rand(3, 3)
print("Random Array: \n", random_array)

random_intergers = np.random.randint(0, 10, size=(2,3))
print("Random integers: \n", random_intergers)

