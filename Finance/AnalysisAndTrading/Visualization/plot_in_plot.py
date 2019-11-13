
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

x = np.linspace(0, 5, 11)
y = x ** 2

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

axes1.plot(x, y)
axes1.set_title('Larger Plot')

axes2.plot(y, x)
axes2.set_title('Smaller Plot')

plt.show()
