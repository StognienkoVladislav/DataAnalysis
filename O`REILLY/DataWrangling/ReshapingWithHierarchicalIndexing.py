

import pandas as pd
import numpy as np
from pandas import DataFrame, Series


data = DataFrame(np.arange(6).reshape((2, 3)),
                 index = pd.Index(['Ohio', 'Colorado'], name = "state"),
                 columns = pd.Index(['one', 'two', 'three'], name = 'number'))

print(data)

result = data.stack()

print(result)

print(result.unstack())

print(result.unstack(0))
print(result.unstack('state'))


s1 = Series([0, 1, 2, 3], index = ['a', 'b', 'c', 'd'])

s2 = Series([4, 5, 6], index = ['c', 'd', 'e'])

data2 = pd.concat([s1, s2], keys=['one', 'two'])

print(data2.unstack())

print(data2.unstack().stack())

print(data2.unstack().stack(dropna = False))


df = DataFrame({'left' : result, 'right' : result + 5},
               columns = pd.Index(['left', 'right'], name = 'side'))

print(df)

print(df.unstack('state'))

print(df.unstack('state').stack('side'))



