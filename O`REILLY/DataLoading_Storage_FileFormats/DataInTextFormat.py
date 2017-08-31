


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('../pydata-book/ch06/ex1.csv')

print(df)


print(pd.read_table('../pydata-book/ch06/ex1.csv', sep = ','))

print(pd.read_csv('../pydata-book/ch06/ex2.csv', header = None))

print(pd.read_csv('../pydata-book/ch06/ex2.csv', names = ['a', 'b', 'c', 'd', 'message']))

names = ['a', 'b', 'c', 'd', 'message']

print(pd.read_csv('../pydata-book/ch06/ex2.csv', names = names, index_col = 'message'))


parsed = pd.read_csv('../pydata-book/ch06/csv_mindex.csv', index_col = ['key1', 'key2'])
print(parsed)


print(list(open('../pydata-book/ch06/ex3.txt')))


result = pd.read_table('../pydata-book/ch06/ex3.txt', sep = '\s+')

print(result)

print(pd.read_csv('../pydata-book/ch06/ex4.csv', skiprows=[0, 2, 3]))

result = pd.read_csv('../pydata-book/ch06/ex5.csv')
print(result)

print(pd.isnull(result))


result = pd.read_csv('../pydata-book/ch06/ex5.csv', na_values=['NULL'])
print(result)


sentinels = {'message' : ['foo', 'Na'], 'something' : ['two']}

print(pd.read_csv('../pydata-book/ch06/ex5.csv', na_values=sentinels))


#Reading Text Files in Pieces

result = pd.read_csv('../pydata-book/ch06/ex6.csv')
print(result)


print(pd.read_csv('../pydata-book/ch06/ex6.csv', nrows=5))

#Drop info with cunksize

chunker = pd.read_csv('../pydata-book/ch06/ex6.csv', chunksize=1000)
print(chunker)


tot = pd.Series([])

for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value = 0)

#tot = tot.order(ascending = False)

print(tot[:10])


#Writing Data Out to Text Format

data = pd.read_csv('../pydata-book/ch06/ex5.csv')

print(data)

dates = pd.date_range('1/1/2000', periods = 7)



#Manually Working with Delimited Formats

import csv

f = open('../pydata-book/ch06/ex7.csv')

reader = csv.reader(f)

for line in reader:
    print (line)


lines = list(csv.reader(open('../pydata-book/ch06/ex7.csv')))

header, values = lines[0], lines[1:]

data_dict = {h: v for h, v in zip(header, zip(*values))}

print(data_dict)



#JSON Data

obj = """
{"name": "Wes",
"places_lived": ["United States", "Spain", "Germany"],
"pet": null,
"siblings": [{"name": "Scott", "age": 25, "pet": "Zuko"},
             {"name": "Katie", "age": 33, "pet": "Cisco"}]
}
"""

import json

result = json.loads(obj)

print(result)

asjson = json.dumps(result)

siblings = pd.DataFrame(result['siblings'], columns = ['name', 'age'])

print(siblings)

