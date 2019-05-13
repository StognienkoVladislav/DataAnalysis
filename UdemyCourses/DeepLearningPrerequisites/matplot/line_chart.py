

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 200)

y = np.sin(x)

plt.plot(x, y)

plt.xlabel("Time")
plt.ylabel("Some title")

plt.show()
