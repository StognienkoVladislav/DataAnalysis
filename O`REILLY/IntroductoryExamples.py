
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

mean_ratings = data.pivot_table('rating', index = 'title',
                                columns = 'gender', aggfunc = 'mean')
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



#Most divisive between male and female

mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']

sorted_by_diff = mean_ratings.sort_index(by = 'diff')
print(sorted_by_diff[:15])

#Reverse order of rows, take first 15 rows
print(sorted_by_diff[::-1][:15])




#Disagreement among viewers

#Standart deviation of rating grouped by title
rating_std_by_title = data.groupby('title')['rating'].std()

#Filter down to active_titles
rating_std_by_title = rating_std_by_title.ix[active_titles]

#Order Series by value in descending order
#print(rating_std_by_title.order(ascending = False)[:10])




###US Baby Names 1880 - 2010




import pandas as pd

names1880 = pd.read_csv('pydata-book/ch02/names/yob1880.txt', names = ['name',
                        'sex', 'births'])

print(names1880)

print(names1880.groupby('sex').births.sum())


#To download all data
#2010 is the last available year right now
years = range(1880, 2011)

pieces = []
columns = ['name', 'sex', 'births']

for year in years:
    path = 'pydata-book/ch02/names/yob%d.txt' % year
    frame = pd.read_csv(path, names = columns)

    frame['year'] = year
    pieces.append(frame)

#Concatenate everything into a single DataFrame
names = pd.concat(pieces, ignore_index = True)

print(names)


#Aggregating the data
total_births = names.pivot_table('births', index = 'year',
                                 columns = 'sex', aggfunc = sum)
print(total_births.tail())


total_births.plot(title = 'Total births by sex and year')
plt.show()


#Particular name
def add_prop(group):
    #Integer division floors
    births = group.births.astype(float)

    group['prop'] = births / births.sum()
    return group

names = names.groupby(['year', 'sex']).apply(add_prop)



print(names)


print(np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1))


#Top 1000 names for each gender
def get_top1000(group):
    return group.sort_index(by = 'births', ascending = False)[:1000]

grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)


#If we do it by self
pieces = []
for year, group in names.groupby(['year', 'sex']):
    pieces.append(group.sort_index(by = 'births', ascending = False)[:1000])

top1000 = pd.concat(pieces, ignore_index=True)




#Analyzing Naming Trends


boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']


#Pivot by year and name
total_births = top1000.pivot_table('births', index = 'year', columns = 'name',
                                   aggfunc = sum)




print(total_births)

subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]
subset.plot(subplots = True, figsize = (12, 10), grid = False,
            title = "Number of births per year")
plt.show()



#Measuring the increase in naming diversity

table = top1000.pivot_table('prop', index = 'year', columns = 'sex',
                            aggfunc = sum)

table.plot(title = 'Sum of table1000.prop by year and sex',
           yticks = np.linspace(0, 1.2, 13), xticks = range(1880, 2020, 10))
plt.show()


df = boys[boys.year == 2010]
print(df)


prop_cumsum = df.sort_index(by = 'prop', ascending = False).prop.cumsum()
print(prop_cumsum[:10])

print(prop_cumsum.searchsorted(0.5))


df = boys[boys.year == 1900]
in1900 = df.sort_index(by = 'prop', ascending = False).prop.cumsum()
print(in1900.searchsorted(0.5) + 1)



def get_quantile_count(group, q = 0.5):
    group = group.sort_index(by = 'prop', ascending = False)
    return group.prop.cumsum().searchsorted(q) + 1

diversity = top1000.groupby(['year', 'sex']).apply(get_quantile_count)
diversity = diversity.unstack('sex')

print(diversity.head())

diversity.plot(title = "Number of popular names in top 50%")
plt.show()


#The `Last Letter` Revolution

#Extract last letter from name column
get_last_letter = lambda x : x[-1]
last_letters = names.name.map(get_last_letter)
last_letters.name = 'last_letter'
table = names.pivot_table('births', index = last_letters,
                          cols = ['sex', 'year'], aggfunc = sum)

subtable = table.reindex(columns = [1910, 1960, 2010], level = 'year')
print(subtable.head())


print(subtable.sum())

letter_prop = subtable / subtable.sum().astype(float)

#Plots for each sex broken down by year

fig, axes = plt.subplot(2, 1, figsize = (10, 8))
letter_prop['M'].plot(kind = 'bar', rot = 0, ax = axes[0], title = 'Male')
letter_prop['F'].plot(kind = 'bar', rot = 0, ax = axes[1], title = 'Female',
                      legend = False)
plt.show()



letter_prop = table / table.sum().astype(float)
dny_ts = letter_prop.ix[['d', 'n', 'y'], 'M'].T
print(dny_ts.head())

dny_ts.plot()
plt.show()



#Boy names that became girl names (and vice versa)

all_names = top1000.name.unique()
mask = np.array(['lesl' in x.lower() for x in all_names])
lesley_like = all_names[mask]
print(lesley_like)


filtered = top1000[top1000.name.isin(lesley_like)]

filtered.groupby('name').births.sum()

table = filtered.pivot_table('births', index = 'year',
                             columns = 'sex', aggfunc = 'sum')
table = table.div(table.sum(1), axis = 0)

print(table.tail())

table.plot(style = {'M' : 'k-', 'F' : 'k--'})

