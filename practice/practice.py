from scipy import interpolate
import numpy as np
from matplotlib import pyplot as plt

x = [-3., -1.8, -0.6, 0.6, 1.8, 3.0 ]
y = [-80.99326205, -17.47362923, -0.57372642, 0.89459696, 18.31473075, 83.71828183]
f = interpolate.interp1d(x, y, kind = "cubic")
print(f(1.9))
