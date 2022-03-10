#get the powers of an array values element-wise.

import pandas as pd
import numpy as np
arr = np.arange(7)
print("Original array:")
print(arr)
print("First array elements raised to powers from second array, element-wise:")
print(np.power(arr, 3))