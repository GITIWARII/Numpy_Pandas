#program to create a null vector of size 10 and update sixth value to 11.

import numpy as np

arr = np.zeros(10, dtype = float)
print(arr)
print("Update sixth value to 11")
arr[7] = float(11)
print(arr)