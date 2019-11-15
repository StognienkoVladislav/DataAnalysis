
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

airline = pd.read_csv('data/airline_passengers.csv', index_col="Month")
airline.dropna(inplace=True)
airline.index = pd.to_datetime(airline.index)

result = seasonal_decompose(airline['Thousands of Passengers'], model='multiplicative')
result.plot()
plt.show()
