#convert a Panda module Series to Python list and it's type.

import pandas as pd

ps = pd.Series([1, 2, 3, 4, 5])
print(ps)
print("DataType of ps is:", type(ps))
print(ps.tolist())
