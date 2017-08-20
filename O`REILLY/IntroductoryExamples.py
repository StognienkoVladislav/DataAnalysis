
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
