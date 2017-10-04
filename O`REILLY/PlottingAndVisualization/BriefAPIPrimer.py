

import matplotlib.pyplot as plt
from numpy.random import randn
import numpy as np


#Figures and Subplot


fig = plt.figure()

ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)

plt.plot(randn(50).cumsum(), 'k--')

_ = ax1.hist(randn(100), bins = 20, color = 'k', alpha = 0.3)

ax2.scatter(np.arange(30), np.arange(30) + 3 * randn(30))

plt.show()


fig, axes = plt.subplots(2, 2, sharex = True, sharey=True)

for i in range(2):
    for j in range(2):
        axes[i, j].hist(randn(500), bins = 50, color = 'k', alpha = 0.5)

plt.subplots_adjust(wspace = 0, hspace = 0)
plt.show()


#Colors, Markers and Line Styles


data = randn(30).cumsum()
plt.plot(data, 'k--', label = 'Default')

plt.plot(data, 'k--', drawstyle = 'steps-post', label = 'steps-post')

plt.legend(loc = 'best')
plt.show()