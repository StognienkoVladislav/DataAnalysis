
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


df = pd.read_csv('tmdb_5000_movies.csv')
print(df[['title', 'revenue', 'budget']].sort_values('revenue')[-10:][::-1])
# df[['title', 'revenue', 'budget']].sort_values('revenue')[-10:][::-1].to_csv('top_revenue')
print(df[['title', 'vote_average', 'vote_count']].sort_values('vote_count')[-10:][::-1])
df[['title', 'vote_average', 'vote_count']].sort_values('vote_count')[-10:][::-1].to_csv('highest_vote_average')
y_formatter = matplotlib.ticker.ScalarFormatter(useOffset=False)

print(df[['runtime', 'vote_average', 'vote_count']].sort_values('vote_count')[-10:][::-1])
print("////////////////////////////////////////")
print(df['runtime'].value_counts().head())

print("////////////////////////////////////////")

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


fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

test_data = df[['popularity', 'budget', 'revenue']].sort_values('revenue')[-10:]
mass = [ test_data['budget'], test_data['revenue']]

for c, z, y_val in zip(['r', 'g'], [10, 0], mass):
    xs = np.arange(10)
    ys = y_val

    #You can provide either a single color or an array. To demonstrate this,
    #the first bar of each set will be colored cyan.
    cs = [c] * len(xs)

    ax.bar(xs, ys, zs = z, zdir = 'y', color = cs, alpha = 0.8)

ax.legend(('budget', 'revenue'))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
