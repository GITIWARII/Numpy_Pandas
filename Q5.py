#Python program to create a 2d array with 1 on the border and 0 inside.


import numpy as np
print("Original array:")
arr = np.ones((5, 5))
print(arr)
arr[1:-1, 1:-1] = 0
print("1 on the border and 0 inside in the array")
print(arr)
