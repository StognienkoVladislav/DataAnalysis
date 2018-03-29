from nltk.book import text6
from nltk import FreqDist
from nltk import bigrams
from nltk import ngrams

fdist = FreqDist(text6)
print(fdist.most_common(10))

bigrams = bigrams(text6)
bigrams_dist = FreqDist(bigrams)
print(bigrams_dist[("Sir", "Robin")])

fourgrams = ngrams(text6, 4)
fourgrams = FreqDist(fourgrams)
print(fourgrams[("father", "smelt", "of", "elderberries")])

fourgrams = ngrams(text6, 4)
for fourgram in fourgrams:
    if fourgram[0] == "coconut":
        print(fourgram)
