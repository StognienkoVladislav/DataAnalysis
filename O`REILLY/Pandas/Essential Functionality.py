


#Reindexing
from pandas import Series
import pandas as pd
import numpy as np
from pandas import DataFrame

obj = Series([4.5, 7.2, -5.3, 3.6], index = ['d', 'b', 'a', 'c'])

obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])

print(obj)

print(obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value = 0))


obj3 = Series(['blue', 'purple', 'yellow'], index = [0, 2, 4])

print(obj3.reindex(range(6), method = 'ffill'))


frame = DataFrame(np.arange(9).reshape((3, 3)),
                  index = ['a', 'c', 'd'],
                  columns  =['Ohio', 'Texas', 'California'])
print(frame)


frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print(frame2)


#Reindexing usin columns

states = ['Texas', 'Utah', 'California']

print(frame.reindex(columns = states))


print(frame.reindex(index = ['a', 'b', 'c', 'd'],
                    method = 'ffill',
                    columns = states))


print(frame.ix[['a', 'b', 'c', 'd'], states])



#Dropping entries from an axis

obj = Series(np.arange(5.), index = ['a', 'b', 'c', 'd', 'e'])

new_obj = obj.drop('c')
print(new_obj)

print(obj.drop(['d', 'c']))


data = DataFrame(np.arange(16).reshape((4, 4)),
                 index = ['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns = ['one', 'two', 'three' 'four'])

print(data.drop(['Colorado', 'Ohio']))
print(data.drop('two', axis = 1))
print(data.drop(['two', 'four'], axis = 1))


#Indexing, selection, and filtering

obj = Series(np.arange(4.), index = ['a', 'b', 'c', 'd'])

print(obj['b'])
print(obj[1])
print(obj[2:4])
print(obj[['b', 'a', 'd']])



print(obj[[1, 3]])
print(obj[obj < 2])

print(obj['b':'c'])

obj['b':'c'] = 5
print(obj)


data = DataFrame(np.arange(16).reshape((4, 4)),
                 index = ['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns = ['one', 'two', 'three', 'four'])
print(data)

print(data['two'])
print(data[['three', 'one']])
print(data[:2])
print(data[data['three'] > 5])

print(data < 5)
data[data < 5] = 0
print(data)


print(data.ix['Colorado', ['two', 'three']])

print(data.ix[['Colorado', 'Utah'], [3, 0, 1]])

print(data.ix[2])

print(data.ix[:'Utah', 'Two'])


print(data.ix[data.three > 5, :3])


#Arithmetic and data alignment


s1 = Series([7.3, -2.5, 3.4, 1.5], index = ['a', 'c', 'd', 'e'])

s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index = ['a', 'c', 'e', 'f', 'g'])

print(s1)
print(s2)

print(s1 + s2)



df1 = DataFrame(np.arange(9.).reshape((3, 3)),
                columns = list('bcd'),
                index = ['Ohio', 'Texas', 'Colorado'])

df2 = DataFrame(np.arange(12.).reshape((4, 3)),
                columns = list('bde'),
                index = ['Utah', 'Ohio', 'Texas', 'Oregon'])

print(df1)
print(df2)


print(df1 + df2)



#Arithmetic methods with fill values

df1 = DataFrame(np.arange(12.).reshape((3, 4)), columns = list('abcd'))

df2 = DataFrame(np.arange(20.).reshape((4, 5)), columns = list('abcde'))

print(df1)
print(df2)

print(df1 + df2)
print(df1.add(df2, fill_value = 0))

print(df1.reindex(columns = df2.columns, fill_value=0))


#add == +
#sub == -
#div == /
#mul == *


#Operations between DataFrame and Series


arr = np.arange(12.).reshape((3, 4))
print(arr)

print(arr[0])
print(arr - arr[0])



frame = DataFrame(np.arange(12.).reshape((4, 3)),
                  columns = list('bde'),
                  index = ['Utah', 'Ohio', 'Texas', 'Oregon'])

series = frame.ix[0]
print(frame)
print(series)

print(frame - series)

series2 = Series(range(3), index = ['b', 'e', 'f'])

print(frame + series2)
#Только пересечение

series3 = frame['d']
print(frame)
print(series3)

print(frame.sub(series3, axis = 0))


#Function application and mapping


frame = DataFrame(np.random.randn(4, 3),
                  columns = list('bde'),
                  index = ['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)
print(np.abs(frame))


f = lambda x : x.max() - x.min()

print(frame.apply(f))
print(frame.apply(f, axis = 1))


def f(x):
    return Series([x.min(), x.max()], index = ['min', 'max'])

print(frame.apply(f))


format = lambda x: '%.2f' % x

print(frame.applymap(format))

print(frame['e'].map(format))


#Sorting and ranking

obj = Series(range(4), index = ['d', 'a', 'b', 'c'])
print(obj.sort_index())



frame  = DataFrame(np.arange(8).reshape((2, 4)),
                   index = ['three', 'one'],
                   columns = ['d', 'a', 'b', 'c'])

print(frame.sort_index())
print(frame.sort_index(axis = 1))

print(frame.sort_index(axis = 1, ascending = False))

obj = Series([4, 7, -3, 2])
print(obj.order())


obj = Series([4, np.nan, 7, np.nan, -3, 2])
print(obj.order())


frame = DataFrame({'b' : [4, 7, -3, 2], 'a' : [0, 1, 0, 1]})

print(frame)
print(frame.sort_index(by = 'b'))

print(frame.sort_index(by = ['a', 'b']))

obj = Series([7, -5, 7, 4, 2, 0, 4])
print(obj.rank())

print(obj.rank(method='first'))
print(obj.rank(ascending=False, method='max'))


frame = DataFrame({'b' : [4.3, 7, -3, 2],
                   'a' : [0, 1, 0, 1],
                   'c' : [-2, 5, 8, -2.5]})

print(frame)
print(frame.rank(axis = 1))



#Axis indexes with duplicate values


obj = Series(range(5), index = ['a', 'a', 'b', 'b', 'c'])

print(obj)

print(obj.index.is_uniqe)

print(obj['a'])
print(obj['c'])


df = DataFrame(np.random.randn(4, 3), index = ['a', 'a', 'b', 'b'])
print(df)
print(df.ix['b'])
