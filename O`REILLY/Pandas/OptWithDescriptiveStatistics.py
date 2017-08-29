
import pandas as pd
import numpy as np
from pandas import DataFrame


df = DataFrame([[1.4, np.nan], [7.1, -4.5],
                [np.nan, np.nan], [0.75, -1.3]],
               index = ['a', 'b', 'c', 'd'],
               columns = ['one', 'two'])
print(df)

print(df.sum()) #by columns

print(df.sum(axis = 1)) #by rows

print(df.mean(axis = 1, skipna = False))

print(df.idxmax())   #index value where the max value

print(df.cumsum())  #accumulations

print(df.describe())

obj = pd.Series(['a', 'a', 'b', 'c'] * 4)
print(obj.describe())



#Correlation and Covariance

import pandas.io.data as web

all_data = {}
for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
    all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2000', '1/1/2010')

price = DataFrame({tic: data['Adj Close']
                    for tic, data in all_data.iteritems()})

volume = DataFrame({tic: data['Volume']
                    for tic, data in all_data.iteritems()})

returns = price.pct_change()
print(returns.tail())


print(returns.MSFT.corr(returns.IBM))

print(returns.MSFT.cov(returns.IBM))

print(returns.corr())

print(returns.cov())

print(returns.corrwith(returns.IBM))

print(returns.corrwith(volume))




#Unique Values, Value Counts, and Membership


obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])

uniques = obj.unique()
print(uniques)

print(obj.value_counts())


print(pd.value_counts(obj.values, sort = False))


mask = obj.isin(['b', 'c'])

print(mask)

print(obj[mask])


data = DataFrame({'Qu1' : [1, 3, 4, 3, 4],
                  'Qu2' : [2, 3, 1, 2, 3],
                  'Qu3' : [1, 5, 2, 4, 4]})

print(data)


result = data.apply(pd.value_counts).fillna(0)

print(result)

