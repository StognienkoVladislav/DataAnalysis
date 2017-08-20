
path = 'pydata-book/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
print(open(path).readline())



import json
records = [json.loads(line) for line in open(path)]


print(records[0])
print(records[0]['tz'])

time_zones = [rec['tz'] for rec in records if 'tz' in rec]

print(time_zones[:10])


#Counting Time Zones in Pure Python

def get_counts(sequence):
    counts = {}

    for x in sequence:
        if x in counts:
            counts[x] += 1

        else:
           counts[x] = 1

        return counts


#2 var
from collections import defaultdict
def get_counts2(sequence):
    counts = defaultdict(int)   #values will initialize to 0
    for x in sequence:
        counts[x] += 1

    return counts


counts = get_counts(time_zones)
print(counts['America/New_York'])
print(len(time_zones))


#Top 10 time zones
def top_counts(count_dict, n = 10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

print(top_counts(counts))


#Standart lib
from collections import Counter
counts = Counter(time_zones)
print(counts.most_common(10))



#Counting Time Zones with pandas


from pandas import DataFrame, Series
import pandas as pd

frame = DataFrame(records)
print(frame)


print(frame['tz'][:10])

#Count
tz_counts = frame['tz'].value_counts()
print(tz_counts[:10])


#Count with 'Unknown'
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
print(tz_counts[:10])


#For plot
import matplotlib.pyplot as plt

tz_counts[:10].plot(kind = 'barh', rot = 0)
plt.show()

print(frame['a'][1])
print(frame['a'][50])
print(frame['a'][51])




results = Series([x.split()[0] for x in frame.a.dropna()])
print(results[:5])

print(results.value_counts()[:8])


################################
cframe = frame[frame.a.notnull()]

#Count of Windows and Not Windows
import numpy as np

operating_system = np.where(cframe['a'].str.contains('Windows'),
                            'Windows', 'Not Windows')

print(operating_system[:5])


#Group By
by_tz_os = cframe.groupby(['tz', operating_system])

agg_counts = by_tz_os.size().unstack().fillna(0)
print(agg_counts[:10])



#Use to sort in ascending order
indexer = agg_counts.sum(1).argsort()
print(indexer[:10])


count_subset = agg_counts.take(indexer)[-10:]
print(count_subset)



count_subset.plot(kind = 'barh', stacked = True)
plt.show()

normed_subset = count_subset.div(count_subset.sum(1), axis = 0)
normed_subset.plot(kind = 'barh', stacked = True)
plt.show()





#MovieLens 1M Data Set

import pandas as pd

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('pydata-book/ch02/movielens/users.dat', sep = '::',
                      header = None, names = unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('pydata-book/ch02/movielens/ratings.dat', sep = '::',
                        header = None, names = rnames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('pydata-book/ch02/movielens/movies.dat', sep = '::',
                       header = None, names = mnames)

print(users[:5])
print(ratings[:5])
print(movies[:5])

print(ratings)



#Merge(join)

data = pd.merge(pd.merge(ratings, users), movies)

print(data)

print(data.ix[0])

#Pivot_table

mean_ratings = data.pivot_table('rating', rows = 'title',
                                cols = 'gender', aggfunc = 'mean')
print(mean_ratings[:5])


#Group by title and size()
ratigns_by_title = data.groupby('title').size()
print(ratigns_by_title[:10])



active_titles = ratigns_by_title.index[ratigns_by_title >= 250]
print(active_titles)

mean_ratings = mean_ratings.ix[active_titles]
print(mean_ratings)



#Top films among female
top_female_ratings = mean_ratings.sort_index(by = 'F', ascending = False)
print(top_female_ratings[:10])



