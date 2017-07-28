import numpy as np
import pylab
import scipy.stats as stats
from pandas import read_csv

measurements = np.random.normal(loc = 20, scale = 5, size = 100)
stats.probplot(measurements, dist = 'norm', plot = pylab)
pylab.show()

pylab.figure()
pData = read_csv('E:/GitHub/DataAnalysis/data/ss06pid.csv')
pData['AGEP'].plot(kind = 'kde', linewidth = 3)
pData['AGEP'][pData['SEX'] == 1].plot(kind = 'kde', linewidth = 3, style = 'orange')

pylab.show()

