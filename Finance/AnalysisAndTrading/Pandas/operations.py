
import numpy as np
import pandas as pd


df = pd.DataFrame({'col1': [1, 2, 3, 4],
                   'col2': [444, 555, 666, 444],
                   'col3': ['abc', 'def', 'ghi', 'xyz']})
print(df.head(), '\n')

# Unique
print(df['col2'].unique(), '\n')

# Value count
print(df['col2'].value_counts(), '\n')

print(df['col2'].apply(lambda x: x*2), '\n')

# Sorting by columns
print(df.sort_values('col2'), '\n')


data = {'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
        'B': ['one', 'one', 'two', 'two', 'one', 'one'],
        'C': ['x', 'y', 'x', 'y', 'x', 'y'],
        'D': [1, 3, 2, 5, 4, 1]}

df = pd.DataFrame(data)
print(df, '\n')

print(df.pivot_table(values='D', index=['A', 'B'], columns=['C']), '\n')

