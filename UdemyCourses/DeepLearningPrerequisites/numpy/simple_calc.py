
import numpy as np


# x1 + x2 = 2200
# 1.5x1 + 4x2 = 5050


A = np.array([[1, 1], [1.5, 4]])

b = np.array([2200, 5050])

print(np.linalg.solve(A, b))
