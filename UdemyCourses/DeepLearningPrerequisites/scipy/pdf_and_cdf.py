
import numpy as np
from scipy.stats import norm


print(norm.pdf(0))

print(norm.pdf(0, loc=5, scale=10))

r = np.random.randn(10)
print(r)

# pdf
print(norm.pdf(r))
print(norm.logpdf(r))

# cdf
print(norm.cdf(r))
print(norm.logcdf(r))
