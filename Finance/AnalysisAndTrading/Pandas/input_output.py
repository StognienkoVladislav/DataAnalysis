
import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('data/example.csv')
print(df, '\n')

# df.to_csv('Output_file', index=False)

df2 = pd.read_excel('data/Excel_Sample.xlsx', sheet_name='Sheet1')

print(df2, '\n')

data = pd.read_html('https://www.some.example.url/example.html')

engine = create_engine('sqlite:///:memory:')

df.to_sql('my_table', engine)

sqldf = pd.read_sql('my_table', con=engine)
print(sqldf, '\n')

