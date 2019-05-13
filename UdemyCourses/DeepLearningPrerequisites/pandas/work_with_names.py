
import numpy as np
import pandas as pd
from datetime import datetime


df = pd.read_csv("../data/international-airline-passengers.csv", engine="python", skipfooter=3)

df.columns = ['month', 'passengers']
print(df.columns)

print(df['passengers'].head())

df['ones'] = 1
print(df.head())

print(datetime.strptime("1949-05", "%Y-%m"))


df['dt'] = df.apply(lambda row: datetime.strptime(row['month'], "%Y-%m"), axis=1)
print(df.head())
print(df.info())
