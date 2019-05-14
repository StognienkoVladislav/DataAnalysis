
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

A = pd.read_csv("../data/data_1d.csv", header=None).as_matrix()

x = A[:, 0]
y = A[:, 1]

# plt.scatter(x, y)

x_line = np.linspace(0, 100, 100)
y_line = 2*x_line + 1

plt.hist(x)
plt.show()

R = np.random.random(100000)
plt.hist(R, bins=20)
plt.show()

y_actual = 2*x + 1
residuals = y - y_actual
plt.hist(residuals)
plt.show()
