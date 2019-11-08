
import numpy as np
import pandas as pd


data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]}


df = pd.DataFrame(data)
print(df, '\n')

by_comp = df.groupby('Company')
print(by_comp.mean(), '\n')
print(by_comp.sum(), '\n')
print(by_comp.std(), '\n')
print(by_comp.count(), '\n')
print(by_comp.max(), '\n')
print(by_comp.min(), '\n')

print(by_comp.describe(), '\n')
