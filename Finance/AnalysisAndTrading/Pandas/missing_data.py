
import numpy as np
import pandas as pd


d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
df = pd.DataFrame(d)

print(df, '\n')

print(df.dropna(), '\n')
print(df.dropna(axis=1), '\n')

# set new value to NA fields
print(df.fillna(value='FILL VALUE'), '\n')

print(df['A'].fillna(value=df['A'].mean()), '\n')
