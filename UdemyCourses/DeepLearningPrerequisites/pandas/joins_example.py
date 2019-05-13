
import numpy as np
import pandas as pd


t1 = pd.read_csv('../data/table1.csv')
t2 = pd.read_csv('../data/table2.csv')

print(t1.head())
print(t2.head())


m = pd.merge(t1, t2, on='user_id')
