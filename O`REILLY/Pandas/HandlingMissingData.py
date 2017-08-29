
import pandas as pd
import numpy as np
from pandas import  DataFrame
from pandas import Series


string_data = Series(['aardvark', 'artichoke', np.nan, 'avocado'])

print(string_data)

print(string_data.isnull())

string_data[0] = None

print(string_data.isnull())




#Filtering Out Missing Data

from numpy import nan as NA


data = Series([1, NA, 3.5, NA, 7])

print(data.dropna())


print(data[data.notnull()])



data = DataFrame([[1., 6.5, 3.], [1., NA, NA],
                 [NA, NA, NA], [NA, 6.5, 3.]])

cleaned = data.dropna()

print(data)

print(cleaned)


print(data.dropna(how = 'all'))     #drop rows that are all NA


data[4] = NA
print(data)

print(data.dropna(axis = 1, how = 'all'))


df = DataFrame(np.random.randn(7, 3))

df.ix[:4, 1 ] = NA
df.ix[:2, 2]  = NA

print(df)

print(df.dropna(thresh = 3))



#Filling in Missing Data

print(df.fillna(0))

print(df.fillna({1: 0.5, 3: -1}))


#always returns a reference to the filled object

_ = df.fillna(0, inplace=True)

print(df)


df = DataFrame(np.random.randn(6, 3))

df.ix[2:, 1] = NA
df.ix[4:, 2] = NA

print(df)

print(df.fillna(method='ffill'))

print(df.fillna(method='ffill', limit = 2))

data = Series([1., NA, 3.5, NA, 7])

print(data.fillna(data.mean()))

