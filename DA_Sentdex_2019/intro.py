
import pandas as pd


df = pd.read_csv("datasets/avocado.csv")
print(df.head())

albany_df = df[df['region'] == "Albany"]
# print(albany_df.head())

# print(albany_df.set_index("Date"))

albany_df = albany_df.set_index("Date")

albany_df.plot()
