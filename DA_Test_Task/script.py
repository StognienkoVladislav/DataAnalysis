import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime

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
# print(data3['SumRevB'].sum())


def calc_sum(data):
    sum = 0.0
    for val in data:
        val = val.replace(',', '.')
        sum += float(val)
    return sum


# Сумма за 2 проекта
# print(calc_sum(data3['SumRevB']))
# print(calc_sum(data3['SumRevA']))

# Ивент / Новый Сервер / Глоб_Обновление
# print(data1['RegDate'].value_counts()[:5])

# Рега
# print(data1['RegSource'].value_counts())

# Страна узера
# print(data1['RegCountry'].value_counts())

# Самый донатный день
# print(data2['DepDate'].value_counts())

# Найбольший донат
# print(data2['Sum'].max())

# Платеж системы
# print(data2['PaymInstr'].value_counts())


"""Затраты/Прибыль"""

print(data3['GameDate'].max(), data3['GameDate'].min())


def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)


game_days = days_between(data3['GameDate'].max(), data3['GameDate'].min())
months = game_days//30 + 1
# print(months)
expenses = months * -100000
print(expenses)

# print(data1[data1['RegSource'] == 'WM']['RegSource'].count())
WM_count = data1[data1['RegSource'] == 'WM']['RegSource'].count()
expenses -= WM_count * 2
print(expenses)

