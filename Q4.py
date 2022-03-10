#to add, subtract, multiple and divide two Pandas Series.

import pandas as pd
ps1 = pd.Series([2, 4, 6, 8, 10])
ps2 = pd.Series([1, 3, 5, 7, 9])
ps = ps1 + ps2
print("Add two Series:")
print(ps)
print("Subtract two Series:")
ps = ps1 - ps2
print(ps)
print("Multiply two Series:")
ps = ps1 * ps2
print(ps)
print("Divide Series1 by Series2:")
ps = ps1 / ps2
print(ps)

