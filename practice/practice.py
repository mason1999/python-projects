from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt

# We have random data points which is in the shape of a sine function
np.random.seed(10)
x = np.linspace(0, 10, num=75)
y = 3.4 * np.sin(1.6 * x) + np.random.normal(size=75)

# define a function in the form of y = asin(bx)
def test_sin(x, a, b):
    return a * np.sin(b * x)

# covariance a 2x2 array for the parameters. 
params, covariance = optimize.curve_fit(test_sin, x, y, p0 = [3, 1])

fitted_y = test_sin(x, params[0], params[1])


fig, ax = plt.subplots()

ax.scatter(x, y)
ax.plot(x, fitted_y)
fig.savefig('out.png')
