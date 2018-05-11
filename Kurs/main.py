
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


df = pd.read_csv('tmdb_5000_movies.csv')
print(df[['title', 'revenue', 'budget']].sort_values('revenue')[-10:][::-1])
# df[['title', 'revenue', 'budget']].sort_values('revenue')[-10:][::-1].to_csv('top_revenue')
print(df[['title', 'vote_average', 'vote_count']].sort_values('vote_count')[-10:][::-1])
df[['title', 'vote_average', 'vote_count']].sort_values('vote_count')[-10:][::-1].to_csv('highest_vote_average')
y_formatter = matplotlib.ticker.ScalarFormatter(useOffset=False)

print(df[['runtime', 'vote_average', 'vote_count']].sort_values('vote_count')[-10:][::-1])
print("////////////////////////////////////////")
print(df['runtime'].value_counts())
# df['runtime'].value_counts()
budget = df['budget'][:10]

popularity = df['popularity'][:10]

df[['budget', 'revenue']].sort_values('budget')[-10:].plot(kind='bar')
# plt.annotate("Location of two axes are adjusted\n"
#              "so that they have equal heights\n"
#              "while maintaining their aspect ratios", (1, 1),
#              xycoords="axes fraction", va="center", ha="center",
#              bbox=dict(boxstyle="round, pad=1", fc="w"))
plt.xlabel('Movies id')
plt.title("Titles")
# df[['title', 'budget']].sort_values('budget')[-10:].plot(kind='bar')
plt.show()
