
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


r = np.random.randn(10000, 2)
r[:, 1] = 5 * r[:, 1] + 2

plt.scatter(r[:, 0], r[:, 1])
plt.axis('equal')
plt.show()
