
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv', sep=',')
print(df.describe())

print('#################')
print(df['registration_day'].describe())
print('#################')
print(df['payment_day'].describe())
print('#################')
print(df['source_id'].describe())
print('#################')
print(df['sum_net'].describe())
