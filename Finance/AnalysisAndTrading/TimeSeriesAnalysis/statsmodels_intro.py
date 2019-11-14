
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import statsmodels.api as sm

df = sm.datasets.macrodata.load_pandas().data

print(df.head(), '\n')

index = pd.Index(sm.tsa.datetools.dates_from_range('1959Q1', '2009Q3'))
df.index = index

gdp_cycle, gdp_trend = sm.tsa.filters.hpfilter(df['realgdp'])

df['trend'] = gdp_trend
df[['realgdp', 'trend']].plot()
plt.show()
