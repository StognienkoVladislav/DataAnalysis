

import pandas as pd
import numpy as np
from pandas import DataFrame, Series


#Integer Indexing



ser = Series(np.arange(3.))
print(ser)


ser2 = Series(np.arange(3.), index = ['a', 'b', 'c'])
print(ser2[-1])

print(ser.ix[:1])

ser3 = Series(range(3), index = [-5, 1, 3])

print(ser3.get_value(2))

frame = DataFrame(np.arange(6).reshape(3, 2), index = [2, 0, 1])
print(frame.row(0))


#Panel Data

import pandas.io.data as web


pdata = pd.Panel(dict((stk, web.get_data_yahoo(stk, '1/1/2009', '6/1/2012'))
                      for stk in ['APPL', 'GOOG', 'MSFT', 'DELL']))


print(pdata)


pdata = pdata.swapaxes('items', 'minor')

print(pdata['Adj Close'])

