import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data1 = pd.read_csv('data/data1.csv', sep=';')
data2 = pd.read_csv('data/data2.csv', sep=';')
data3 = pd.read_csv('data/data3.csv', sep=';')
# print(data1.head())
# print('##############')
# print(data2.head())
# print('##############')
# print(data3['GameHour'].head())

# print(data3[data3['GameHour'] == 7])

# print(data1['RegCountry'].describe())
# print(data1['RegCountry'].value_counts())

info = {}
"""
for i, val in data1.head().iterrows():
    print(val)
    reg_data = val['RegDate']
    dep_data = data2[data2['ID'] == val['ID']]['DepDate']
    game_data = data3[data3['ID'] == val['ID']]['GameDate']
    info[val['ID']] = [reg_data, dep_data, game_data]

print(val for val in info)
"""

# print(pd.to_numeric(data3['SumRevA'], errors='coerce').sum())
# print(pd.to_numeric(data3['SumRevB'], errors='coerce').sum())

# print(data3['SumRevB'].sum())
sum = '0.0'
for val in data3['SumRevB']:
    if type(val) != 0:
        print(sum)
        check = val.split(',')
        print(check)
        check = eval(str(check[0]) + ('0.{}'.format(check[1])))
        print(check)
        sum = eval(str(sum) + val)
    else:
        sum += eval(str(sum) + str(val))
print(sum)
# print(sum(str(v) for v in data3['SumRevB']))
