
import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df, '\n')

print(df['W'], '\n')

df['new'] = df['W'] + df['Y']
print(df, '\n')

df.drop('new', axis=1, inplace=True)
print(df, '\n')

print(df.loc['B', 'Y'], '\n')
print(df.loc[['A', 'B'], ['W', 'Y']], '\n')

result_df = df[df['W']>0]
print(result_df[['Y', 'X']])

print(df[(df['W'] > 0) & (df['Y'] > 1)])
