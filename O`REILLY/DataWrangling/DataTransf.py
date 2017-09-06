
import pandas as pd
import numpy as np
from pandas import DataFrame, Series


#Removing Duplicates

data = DataFrame({'k1' : ['one'] * 3 + ['two'] * 4,
                  'k2' : [1, 1, 2, 3, 3, 4, 4]})

print(data)

print(data.duplicated())

print(data.drop_duplicates())

data['v1'] = range(7)

print(data.drop_duplicates(['k1']))

print(data.drop_duplicates(['k1', 'k2']))


#Transforming Data Using a Function or Mapping

data = DataFrame({'food' : ['bacon', 'pulled pork', 'bacon', 'Pastrami',
                            'corned beef', 'Bacon', 'pastrami', 'honey ham',
                            'nova lox'],
                  'ounces' : [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

print(data)

meat_to_animal = {
    'bacon' : 'pig',
    'pulled pork' : 'pig',
    'pastrami' : 'cow',
    'corned beef' : 'cow',
    'honey ham' : 'pig',
    'nova lox' : 'salmon'
}


data['animal'] = data['food'].map(str.lower).map(meat_to_animal)
print(data)


print(data['food'].map(lambda  x: meat_to_animal[x.lower()]))


#Replacing Values

data = Series([1., -999., 2., -999., -1000., 3.])

print(data)

print(data.replace(-999, np.nan))

print(data.replace([-999, -1000], np.nan))

print(data.replace([-999, -1000], [np.nan, 0]))

print(data.replace({-999 : np.nan, -1000 : 0}))


#Renaming Axis Indexes

data = DataFrame(np.arange(12).reshape(3, 4),
                 index = ['Ohio', 'Colorado', 'New York'],
                 columns = ['one', 'two', 'three', 'four'])

print(data.index.map(str.upper))


data.index = data.index.map(str.upper)

print(data)

print(data.rename(index = str.title, columns = str.upper))

print(data.rename(index = {'OHIO' : 'INDIANA'},
                  columns = {'three' : 'peekaboo'}))

#Always returns a reference to a DataFrame

_ = data.rename(index = {'OHIO' : 'INDIANA'}, inplace=True)
print(data)


#Discretization and Binning

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]

bins = [18, 25, 35, 60, 100]

cats = pd.cut(ages, bins)

print(cats)

print(cats.codes)

print(pd.value_counts(cats))

print(pd.cut(ages, [18, 26, 36, 61, 100], right = False))       #Не включая

group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']

print(pd.cut(ages, bins, labels = group_names))

