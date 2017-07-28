import numpy as np
import pylab
import scipy.stats as stats
from numpy.matlib import randn
from pandas import read_csv, qcut, DataFrame, scatter_matrix

from ExploratoryAnalysis import remove_border, hexbin

measurements = np.random.normal(loc = 20, scale = 5, size = 100)
stats.probplot(measurements, dist = 'norm', plot = pylab)
pylab.show()

pylab.figure()
pData = read_csv('E:/GitHub/DataAnalysis/data/ss06pid.csv')
pData['AGEP'].plot(kind = 'kde', linewidth = 3)
pData['AGEP'][pData['SEX'] == 1].plot(kind = 'kde', linewidth = 3, style = 'orange')

#scatterplot --size matters
pData.plot(x = 'JWMNP', y = 'WAGP', style = 'o', markersize = 3)

pylab.show()

df = DataFrame(randn(1000, 4), columns = ['a', 'b', 'c', 'd'])
scatter_matrix(df, alpha = 0.2, figsize = (6, 6), diagonal = 'kde')

pylab.show()

x = np.random.normal(size=10500)
y = np.random.normal(size=10500)
pylab.plot(x, y, 'o')
pylab.show()

##############################################################
#Diamonds

diamonds = read_csv('E:/GitHUb/DataAnalysis/data/diamonds.csv')

#the raw data
x = diamonds.carat[diamonds.carat < 2]
y = diamonds.price[diamonds.carat < 2]
pylab.plot(x, y, 'o', mec ='none', alpha = .5)

#fit and overplot a 2nd order polynomial
params = np.polyfit(x, y, 2)
xp = np.linspace(x.min(), 2, 20)
yp = np.polyval(params, xp)
pylab.plot(xp, yp, 'k')

#overplot an error band
sig = np.std(y - np.polyval(params, x))
pylab.fill_between(xp, yp - sig, yp + sig, color = 'k', alpha = 0.2)

pylab.xlabel('Carat')
pylab.ylabel('Price')
pylab.xlim(0, 2)
remove_border()
pylab.show()

##############################################################
#Heat Map

x = np.random.normal(size = 100500)
y = np.random.normal(size = 100500)
hexbin(x, y)
pylab.show()