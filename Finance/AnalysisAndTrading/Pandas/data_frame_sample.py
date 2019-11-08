
import numpy as np
import pandas as pd

from numpy.random import randn

# Index levels
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])
print(df, '\n')

print(df.loc['G1'], '\n')
print(df.loc['G1'].loc[2], '\n')

df.index.names = ['Groups', 'Num']
print(df, '\n')

# in G1 and G2 where Num == 1
print(df.xs(1, level='Num'), '\n')
