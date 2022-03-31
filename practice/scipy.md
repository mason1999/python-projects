# Table of contents

1. [introduction](#1)
2. [scipy.optimze](#2)
3. [minimisation](#3)
4. [curve fitting](#4)
5. [root finding](#5)
6. [scipy.interpolate](#6)
7. [1D interpolation](#7)
8. [2D interpolation](#8)
9. [scipy.stats](#9)
10. [continuous distributions](#10)
11. [discrete distributions](#11)
12. [probability mass/density function](#12)
13. [cumulative distribution function](#13)
14. [percentage point function](#14)

# introduction <a name = "1"></a>

Run: 

    pip3 install scipy

A list of the sub-packages we will be focusing on from the `scipy` package are: 
- `cluster` (clustering algorithms)
- `constants` (physical and mathematical constants)
- `fftpack` (fast fourier transform routines)
- `integrate` (integration and ordinary differential equation solvers)
- `interpolate` (interpolation and smooting splines)
- `io` (input and output)
- `linalg` (linear algebra)
- `ndimage` (n-dimesnional image processing)
- `odr` (orthogonal distance regression)
- `optimize` (optimization and root-finding routines)
- `signal` (signal processing)
- `sparse` (sparse matrices and associated routines)
- `spatial` (spatial data structures and algorithms)
- `special` (special functions)
- `stats` (statistical distributions and functions)

For example we would write something like: 

    from scipy inport interpolate, optimize, stats

# scipy.optimze <a name = "2"></a>

Optimisation is about the selection of the best element or function from a range of choices based on some criteria. 

The `scipy.optimize` subpackage contains five main categories relating to optimisation. 

- Unconstained and constrained minimisation of multivariate scalar functions
- Global optimisation routines
- Curve fitting and regression algorithms
- Root rfinders and scalar univariate functions minimizers
- Multivariate equation system solvers using a range of methods 

# minimisation <a name = "3"></a>

We want to minimise the function $$y = 5x^6 - 2x + 1$$

Using matplotlib this is what the function looks like from $x = 0$ to $x = 1$

    from matplotlib import pyplot as plt
    import numpy as np 
    # make 100 points between 0 and 1 inclusivley
    x = np.linspace(0, 1, 100)
    # obtain our y values
    y = 5 * (x**6) - 2 * x + 1 
    # plot our function:
    fig, ax = plot.subplots()
    ax.plt(x, y, 'red')
    ax.set_title('$y = 5x^5 - 2x + 1$')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    fig.savefig('out.png')

From the plot we can infer that the minimum is between $x = 0.6$ and $x = 0.65$. 

We then use the `minimize_scalar()` function to find the exact position of the minimum value: 

    from scipy.optimize import minimize_scalar

    def function(x):
        return 5 * (x**6) - 2 * x + 1

    print(minimize_scalar(function))

The output gives us a few things:

- `fun`: the `y` value at the minimum. 
- `x`: the `x` value at the minimum. 
- `success`: is `True` when a minimum has been found. 

# curve fitting <a name = "4"></a>


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

# root finding <a name = "5"></a>
# scipy.interpolate <a name = "6"></a>
# 1D interpolation <a name = "7"></a>
# 2D interpolation <a name = "8"></a>
# scipy.stats <a name = "9"></a>
# continuous distributions <a name = "10"></a>
# discrete distributions <a name = "11"></a>
# probability mass/density function <a name = "12"></a>
# cumulative distribution function <a name = "13"></a>
# percentage point function <a name = "14"></a>
