
import pandas as pd
import numpy as np
from pandas import Series, DataFrame


data = Series(np.random.randn(10),
              index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                     [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])


print(data)


print(data.index)

print(data['b'])
print(data['b' : 'c'])
print(data.ix[['b', 'd']])


print(data[:, 2])

print(data.unstack())

print(data.unstack().stack())


frame = DataFrame(np.arange(12).reshape((4, 3)),
                  index = [['a', 'a', 'b', 'b'],
                           [1, 2, 1, 2]],
                  columns=[['Ohio', 'Ohio', 'Colorado'],
                           ['Green', 'Red', 'Green']])

print(frame)


frame.index.names = ['key1', 'key2']

frame.columns.names = ['state', 'color']

print(frame)


print(frame['Ohio'])



#Reordering and Sorting Levels

print(frame.swaplevel('key1', 'key2'))

print(frame.sortlevel(1))

print(frame.swaplevel(0, 1).sortlevel(0))



#Summary Statistics by Level

print(frame.sum(level = 'key2'))
print(frame.sum(level = 'color', axis = 1))



#Using a DataFrame`s Columns

frame = DataFrame({'a' : range(7), 'b' : range(7, 0, -1),
                   'c' : ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                   'd' : [0, 1, 2, 0, 1, 2, 3]})

print(frame)


frame2 = frame.set_index(['c', 'd'])
print(frame2)


print(frame.set_index(['c', 'd'], drop = False))

print(frame2.reset_index())

