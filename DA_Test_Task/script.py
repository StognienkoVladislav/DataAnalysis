import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

from datetime import datetime

data1 = pd.read_csv('data/data1.csv', sep=';')
data2 = pd.read_csv('data/data2.csv', sep=';')
data3 = pd.read_csv('data/data3.csv', sep=';')
# print(data1.head())
# print('##############')
# print(data2.head())
# print('##############')
# print(data3['GameHour'].head())

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


def calc_sum(data):
    sum = 0.0
    for val in data:
        val = val.replace(',', '.')
        sum += float(val)
    return sum


# Сумма за 2 проекта
product_a = calc_sum(data3['SumRevA'])
product_b = calc_sum(data3['SumRevB'])

# Найбольший донат
max_donat = data2['Sum'].max()

"""Затраты/Прибыль"""

print(data3['GameDate'].max(), data3['GameDate'].min())


def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)


game_days = days_between(data3['GameDate'].max(), data1['RegDate'].min())
months = game_days//30 + 1
# print(months)
expenses = months * -100000
# print(expenses)

# print(data1[data1['RegSource'] == 'WM']['RegSource'].count())
WM_count = data1[data1['RegSource'] == 'WM']['RegSource'].count()
expenses -= WM_count * 2
# print(expenses)

percents = [10000, 1000, 100]

users_id = data2['ID'].unique()
"""
for user in users_id:
    for date in range(1, 12):
        summ = calc_sum(data2.query("ID=={} and '2016-0{}-01'<=DepDate<'2016-0{}-01'".format(user, date, date+1))['Sum'])
        # print(summ)
        # print(expenses)
        if summ > percents[0]:
            expenses -= summ*0.2
        elif summ > percents[1]:
            expenses -= summ*0.15
        elif summ > percents[2]:
            expenses -= summ*0.1
        else:
            expenses -= summ*0.05
        # print(expenses)
    for date in range(1, 3):
        summ = calc_sum(data2.query("ID=={} and '2017-0{}-01'<=DepDate<'2017-0{}-01'".format(user, date, date+1))['Sum'])
        # print(summ)
        # print(expenses)
        if summ > percents[0]:
            expenses -= summ * 0.2
        elif summ > percents[1]:
            expenses -= summ * 0.15
        elif summ > percents[2]:
            expenses -= summ * 0.1
        else:
            expenses -= summ * 0.05
        # print(expenses)
    print(expenses)
print(expenses)
"""
expenses_demo = -2151976.5058011217

reports = {'Expenses': expenses_demo, 'Max_deposit': max_donat, 'Prod_A_revenue': product_a,
           'Prod_B_revenue': product_b}

root = ET.Element("root")
doc = ET.SubElement(root, "report")

for key, val in reports.items():
    ET.SubElement(doc, key).text = str(val)

# Ивент / Новый Сервер / Глоб_Обновление
top_5_reg_days = data1['RegDate'].value_counts()[:5]

# Рега
reg_source = data1['RegSource'].value_counts()

# Страна узера
users_in_the_country = data1['RegCountry'].value_counts()

# Самый донатный день
top_5_deposit_days = data2['DepDate'].value_counts()[:5]

# Платеж системы
payment_systems = data2['PaymInstr'].value_counts()

doc = ET.SubElement(root, "detailed_report")

detailed_reports = [top_5_reg_days, reg_source, users_in_the_country, top_5_deposit_days, payment_systems]
description = ["Top_5_registration_days", 'Registration_source', 'Users_in_the_country',
               "Top_5_deposits_days", "Payment_systems"]
for key, val in zip(description, detailed_reports):
    for k, info in val.items():
        ET.SubElement(doc, key).text = '{} - {}'.format(str(k), str(info))

tree = ET.ElementTree(root)
tree.write("analytical_report.xml")

