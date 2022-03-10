#to add a border (filled with 0's) around an existing array.

import numpy as np

print("Original array:")
arr = np.ones((3, 3))
print(arr)

print("border (filled with 0's) around an existing array:")

print(np.pad(arr, pad_width = 1, mode = 'constant', constant_values = 0))
