
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("../data/train.csv")

print(df.shape)


M = df.values
print(M)


im = M[0, 1:]

im = im.reshape(28, 28)

plt.imshow(255-im, cmap='gray')
plt.show()
