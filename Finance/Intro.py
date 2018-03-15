
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web
from matplotlib import style

style.use("ggplot")
"""
    start = dt.datetime(2000, 1, 1)
    end = dt.datetime(2016, 12, 31)
    
    df = web.DataReader('TSLA', "yahoo", start, end)
    df = web.get_data_google("TSLA", start, end)
    print(df.head())
    
    df.to_csv('tsla.csv')
"""
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)
df[['High', 'Low']].plot()

df["100ma"] = df["Close"].rolling(window=100, min_periods=0).mean()
print(df.head())

ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(df.index, df['Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

plt.show()