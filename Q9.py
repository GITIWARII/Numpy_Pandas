#append values to the end of an array.

import numpy as np

print("Original array:")
arr = np.arange(10, 40, 10)
print(arr)
print("After append values to the end of the array:")
print(np.append(arr, np.arange(40, 100, 10)))