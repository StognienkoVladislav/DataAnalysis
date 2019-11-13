
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data/walmart_stock.csv', index_col='Date', parse_dates=True)
print(df.head(), '\n')

# Close 20 MA
df['Close: 20 Day Mean'] = df['Close'].rolling(20).mean()

# Upper = 20MA + 2*std(20)
df['Upper'] = df['Close: 20 Day Mean'] + 2*(df['Close'].rolling(20).std())

# Lower = 20MA - 2*std(20)
df['Lower'] = df['Close: 20 Day Mean'] - 2*(df['Close'].rolling(20).std())

# Close
df[['Close', 'Close: 20 Day Mean', 'Upper', 'Lower']].plot(figsize=(16, 6))
plt.show()
