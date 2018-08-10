import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

"""
Запрос для БД

SELECT COUNT(*) over() all_counts, COUNT(payments.sums)count_payments, SUM(payments.sums) sum_payments
FROM users
JOIN countries ON users.countriesid = countries.id AND countries.country = 'Ukraine'
JOIN payments ON users.id= payments.usersid
WHERE users.first_name = 'Ivan'
GROUP BY payments.usersid;

"""

df = pd.read_csv('data.csv', sep=',')
print(df.describe())

# Общий анализ данных
print('#################')
print(df['registration_day'].describe())
print('#################')
print(df['payment_day'].describe())
print('#################')
print(df['source_id'].describe())
print('#################')
print(df['sum_net'].describe())

df2 = df.copy()
# Для 1 вида
# df2 = df2[df2['source_id'] == 1]

# Для 2 вида
# df2 = df2[df2['source_id'] == 2]

# Общий вариант

df2 = df2.rename(columns={'payment_day': 'Days'})
df2['Days'] = pd.DatetimeIndex(df2['Days'])

# Визуализация текущих данных

ax = df2.set_index('Days').plot(figsize=(12, 8))
ax.set_ylabel("Payment value")
ax.set_xlabel('Date')
plt.show()

# Прогнозирование
my_model = Prophet(interval_width=0.95)
my_model.fit(df2)

future_dates = my_model.make_future_dataframe(periods=30, freq="day")
print(future_dates.tail())

forecast = my_model.predict(future_dates)

# визуализации прогнозируемых данных
# Prophet показывает значения временных рядов (черные точки),
# прогнозируемые значения (синяя линия)
# и интервалы неопределенности прогнозов (синие заштрихованные области).
my_model.plot(forecast, uncertainty=True)

# компоненты прогнозов
my_model.plot_components(forecast)
