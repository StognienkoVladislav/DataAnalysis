
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


# r = np.random.randn(10000)

r = 10*np.random.randn(10000) + 5

plt.hist(r, bins=100)
plt.show()
