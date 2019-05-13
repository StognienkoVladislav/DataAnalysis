
import numpy as np
import pandas as pd


X = pd.read_csv("../data/data_2d.csv", header=None)

print(X.head())

M = X.values
print(type(M))
