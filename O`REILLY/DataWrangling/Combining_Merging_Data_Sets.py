


#DataBase-style DatqaFrame Merges

import pandas as pd
import numpy as np
from pandas import DataFrame, Series

df1 = DataFrame({'key' : ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data': range(7)})

df2 = DataFrame({'key' : ['a', 'b', 'd'],
                 'data2' : range(3)})

print(df1)
print(df2)


#Many-to-one

print(pd.merge(df1, df2))

print(pd.merge(df1, df2, on = 'key'))

df3 = DataFrame({'lkey' : ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1' : range(7)})

df4 = DataFrame({'rkey' : ['a', 'b', 'd'],
                 'data2' : range(3)})

print(pd.merge(df3, df4, left_on='lkey', right_on='rkey'))


#Inner joins   (left, right, outer)

print(pd.merge(df1, df2, how = 'outer'))


df1 = DataFrame({'key' : ['b', 'b', 'a', 'c', 'a', 'b'],
                 'data1' : range(6)})

df2 = DataFrame({'key' : ['a', 'b', 'a', 'b', 'd'],
                 'data2' : range(5)})

print(df1)
print(df2)

#Many-to-many
print(pd.merge(df1, df2, on = 'key', how = 'left'))


print(pd.merge(df1, df2, how = 'inner'))


left = DataFrame({'key1' : ['foo', 'foo', 'bar'],
                  'key2' : ['one', 'two', 'one'],
                  'lval' : [1, 2, 3]})

right = DataFrame({'key1' : ['foo', 'foo', 'bar', 'bar'],
                   'key2' : ['one', 'one', 'one', 'two'],
                   'rval' : [4, 5, 6, 7]})

print(pd.merge(left, right, on = ['key1', 'key2'], how = 'outer'))


print(pd.merge(left, right, on = 'key1'))

print(pd.merge(left, right, on = 'key1', suffixes=('_left', '_right')))



#Merging on Index

left1 = DataFrame({'key' : ['a', 'b', 'a', 'a', 'b', 'c'],
                   'value' : range(6)})

right1 = DataFrame({'group_val' : [3.5, 7]},
                   index = ['a', 'b'])

print(left1)
print(right1)


print(pd.merge(left1, right1, left_on = 'key', right_index=True))

print(pd.merge(left1, right1, left_on='key', right_index=True, how = 'outer'))


lefth = DataFrame({'key1' : ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                   'key2' : [2000, 2001, 2002, 2001, 2002],
                   'data' : np.arange(5.)})

righth = DataFrame(np.arange(12).reshape((6, 2)),
                   index = [['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
                            [2001, 2000, 2000, 2000, 2001, 2002]],
                   columns=['event1', 'event2'])

print(lefth)
print(righth)
