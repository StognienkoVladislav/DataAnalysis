
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal as mvn


cov = np.array([[1, 0.8], [0.8, 3]])

mu = np.array([0, 2])

r = mvn.rvs(mean=mu, cov=cov, size=1000)

plt.scatter(r[:, 0], r[:, 1])
plt.axis('equal')
plt.show()
