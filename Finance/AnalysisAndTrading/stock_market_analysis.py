
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import pandas_datareader
import pandas_datareader.data as web

from pandas.plotting import scatter_matrix


start = datetime.datetime(2012, 1, 1)
end = datetime.datetime(2017, 1, 1)

tesla = web.get_data_yahoo('TSLA', start=start, end=end)

print(tesla.head(), '\n')

ford = web.get_data_yahoo('F', start=start, end=end)
print(ford.head(), '\n')

gm = web.get_data_yahoo('GM', start=start, end=end)
print(gm.head(), '\n')

# Opening Prices
tesla['Open'].plot(label='Tesla', figsize=(12, 8), title='Opening Prices')
gm['Open'].plot(label='GM')
ford['Open'].plot(label='Ford')
plt.legend()
plt.show()

# Volume Traded
tesla['Volume'].plot(label='Tesla', figsize=(16, 8), title='Volume Traded')
gm['Volume'].plot(label='GM')
ford['Volume'].plot(label='Ford')
plt.legend()
plt.show()

# Total Traded
tesla['Total Traded'] = tesla['Open']*tesla['Volume']
ford['Total Traded'] = ford['Open']*ford['Volume']
gm['Total Traded'] = gm['Open']*gm['Volume']

tesla['Total Traded'].plot(label='Tesla', figsize=(16, 8))
gm['Total Traded'].plot(label='GM')
ford['Total Traded'].plot(label='Ford')
plt.legend()
plt.show()

# Moving Averages
gm['MA50'] = gm['Open'].rolling(50).mean()
gm['MA200'] = gm['Open'].rolling(200).mean()
gm[['Open', 'MA50', 'MA200']].plot(figsize=(16, 8))
plt.legend()
plt.show()

# Scatter matrix plot
car_comp = pd.concat([tesla['Open'], gm['Open'], ford['Open']], axis=1)
car_comp.columns = ['Tesla Open', 'GM Open', 'Ford Open']
scatter_matrix(car_comp, figsize=(8, 8), alpha=0.2, hist_kwds={'bins': 50})
plt.show()

