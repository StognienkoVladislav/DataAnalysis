

import pandas as pd
import numpy as np
from pandas import DataFrame, Series


frame = pd.read_csv('../pydata-book/ch06/ex1.csv')

print(frame)



#Using HDF5 Format


store = pd.HDFStore('mydata.h5')
store['obj1'] = frame

store['obj1_col'] = frame['a']

print(store)


#Reading Excel Files

xls_files = pd.ExcelFile('data.xls')

table = xls_files.parse('Sheet1')



#HTML and Web APIs

import requests

url = 'http://serch.twitter.com/serach.json?q=python%20pandas'

resp = requests.get(url)

print(resp)


import json

data = json.loads(resp.text)

print(data.keys())



tweet_fields = ['created_at', 'from_user', 'id', 'text']

tweets = DataFrame(data['results'], columns=tweet_fields)

print(tweets)

print(tweets.ix[7])


#Interacting with Databases


import sqlite3

query = """
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20),
c REAL,         d INTEGER
);"""


con = sqlite3.connect(':memory:')
con.execute(query)
con.commit()

data = [('Atlanta', 'Georgia', 1.25, 6),
        ('Tallahassee', 'Florida', 2.6, 3),
        ('Sacramento', 'California', 1.7, 5)]
stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"

con.executemany(stmt, data)
con.commit()


cursor = con.execute('select * from test')

rows = cursor.fetchall()

print(rows)

print(cursor.description)


