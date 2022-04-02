import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt

# std dev = 13 and mean = 65. Find P(X <= 60)

x = binom.pmf(5, n = 10, p = 0.3)
print(x)
