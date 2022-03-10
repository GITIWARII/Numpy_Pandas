#to convert a list and tuple into arrays.

import numpy as np
new_list = [1, 2, 3, 4, 5, 6, 7, 8]
print("List to array:")
print(np.array(new_list))
new_tuple = ((8, 4, 6), (1, 2, 3))
print("Tuple to array:")
print(np.array(new_tuple, ndmin=2))