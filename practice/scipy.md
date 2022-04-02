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
Given some points of data (in this example we made it up), we:
1. Assume a function we want to fit (e.g $y = asin(bx)$ )
2. Use the `optimize.curve_fit(func, xdata, ydata, list of initial paramters)`
3. Use the parameters you get from this function to make the fitted y values 
4. Plot them with `ax.plot(x, y)` 


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
1. Define the function to be found 
2. use the  `optimize.root(function, x0 = initial_guess)`
3. get the `x` attribute. That is `optimize.root(function, x0 = initial_guess).x`


        from scipy import optimize

        def f(x):
            return -2*x**3 + -5*x**2 + 1

        print(optimize.root(f, x0=-2.6).x)
        print(optimize.root(f, x0=-0.5).x)
        print(optimize.root(f, x0=0.4).x)

4. There are different root finding methods. For example we could use newton's method with `optimize.newton(function, x0 = initial_guess)`
        from scipy import optimize

        def f(x):
            return -2*x**3 + -5*x**2 + 1

        print(optimize.newton(f, x0=0.4))
# scipy.interpolate <a name = "6"></a>
Interpolation is about determining a function that approximates points between the given data points.

The key difference between interpolation and curve fitting is that the interpolated function must pass through all the fixed data points. In curve fitting the function only describes the general shape of the data, it doesn't need to pass through the given points.

There are four main categories of functions of the `scipy.interpolate` package.

- 1-D interpolation (`interp1d`)
- Multivariate data interpolation (`griddata`)
- Spline interpolation
- Using radial basis functions for smoothing/interpolation
# 1D interpolation <a name = "7"></a>
To interpolate we:
1. Use the given observations `x`, `y` and `interpolate.interp1d(x, y, kind = ...)` (where `kind` is the type of graph  you'd like to interpolate) to get an interpolation function/object
2. This object is a function which we can use to evalate values. 

A very simple example:

    from scipy import interpolate
    import numpy as np
    from matplotlib import pyplot as plt

    # x values of data point
    x = [-3., -1.8, -0.6, 0.6, 1.8, 3.0 ]
    # y values of data points
    y = [-80.99326205, -17.47362923, -0.57372642, 0.89459696, 18.31473075, 83.71828183]
    # interpolate a cubic function. Let this cubic function be 'f'
    f = interpolate.interp1d(x, y, kind = "cubic")
    # print the value of f(1.9)
    print(f(1.9))

A more advanced example:

    import numpy as np
    import matplotlib.pyplot as plt
    from scipy import interpolate

    # interpolation function/object?
    x = np.linspace(-3, 3, num=6)
    y = 3*x**3 - 2*x**2
    nearest_interp = interpolate.interp1d(x, y, kind='nearest')
    linear_interp = interpolate.interp1d(x, y, kind='linear')
    cubic_interp = interpolate.interp1d(x, y, kind='cubic')


    interp_samples = np.linspace(-3, 3, 100)
    # figure and axis
    fig, ax = plt.subplots()
    # plot the results
    ax.scatter(x, y, label='Original Points')
    ax.plot(interp_samples, nearest_interp(interp_samples), label='Nearest')
    ax.plot(interp_samples, linear_interp(interp_samples), label='Linear')
    ax.plot(interp_samples, cubic_interp(interp_samples), label='Cubic')
    ax.legend(loc='best')
    fig.savefig('out.png')
# 2D interpolation <a name = "8"></a>

    import numpy as np
    from scipy.interpolate import interp2d
    import matplotlib.pyplot as plt

    # data
    x = np.linspace(0, 5, 10)
    y = np.linspace(0, 5, 10)
    X, Y = np.meshgrid(x, y)

    Z = np.sin(np.pi*X/2) + np.cos(np.pi*Y/2)

    # interpolated points
    x_interp = np.linspace(0, 5, 50)
    y_interp = np.linspace(0, 5, 50)
    g = interp2d(x, y, Z, kind = 'cubic') # interpolation object/function
    z_interp = g(x_interp, y_interp)

    grid_x_interp, grid_y_interp = np.meshgrid(x_interp, y_interp)

    # plotting
    fig, ax = plt.subplots()
    ax.pcolormesh(grid_x_interp, grid_y_interp, z_interp)
    fig.savefig('out.png')
# scipy.stats <a name = "9"></a>
The `scipy.stats` subpackage contains a very large range probability distributions and statistical functions.

This package includes:

- Continuous distributions
- Multivariate distributions
- Discrete distributions
- Summary statistics
- Frequency statistics
- Correlation functions
- Statistical tests

The scipy.stats subpackage contains three classes of distributions:

- `rv_continuous`: continuous random variables
- `rv_discrete`: discrete random variables
- `rv_histogram`: generates a distribution given by a histogram

Each of these classes of distributions have the same methods.
# continuous distributions <a name = "10"></a>

These distributions have a `rvs` method to generate '`size`' number of random variates. The `rvs` method takes in a `loc` (location) and a `scale` argument. By default the `loc` parameter is 0, and the `scale` parameter is 1.

Note: Because we're generating random variates at each run of the program, the graph will not look exactly the same each time.

**UNIFORM DISTRIBUTION**

`uniform` provides a constant distribution between `loc` and `loc + scale`


    import numpy as np
    from scipy.stats import uniform
    import matplotlib.pyplot as plt

    # generating the 10000 for X ~ unif(2, 3) = unif(loc, loc + scale)
    uniform_data = uniform.rvs(size=100, loc=2, scale=1)

    # histogram plot
    fig, ax = plt.subplots()
    ax.hist(uniform_data, bins=100)
    ax.set_xlim(1, 4)
    ax.set_ylim(0, 5)
    ax.set_xlabel('Distribution')
    ax.set_ylabel('Frequency')
    ax.set_title('Uniform distribution')
    fig.savefig('out.png')

**NORMAL DISTRIBUTION**


    import numpy as np
    from scipy.stats import norm
    import matplotlib.pyplot as plt

    # generating 1000 form X ~ N(menan = 3, stdev = 0.5)
    normal_data = norm.rvs(size=1000, loc=3, scale=0.5)

    # histogram plot
    plt.hist(normal_data, bins=100)
    plt.xlim(1, 5)
    plt.ylim(0, 50)
    plt.xlabel('Distribution')
    plt.ylabel('Frequency')
    plt.title('Normal distribution')
    plt.savefig('out.png')
# discrete distributions <a name = "11"></a>

**BINOMIAL DISTRIBUTION**

Binomial distributions describe the probability of $n$ successes for some number of repeated trials, where each trial only has two possible outcomes - success or failure.


The number of trials is passed in as the parameter `n`, and the probability of success for a given trial is given by parameter `p`. Size indicates the number of times to repeat the `n` trials.


    from scipy.stats import binom
    import matplotlib.pyplot as plt

    # generating the binomial data
    binomial_data = binom.rvs(size=1000, n=10, p=0.5)

    # histogram plot
    plt.hist(binomial_data, bins=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    plt.xlim(0, 18)
    plt.ylim(0, 300)
    plt.xlabel('Number of successes')
    plt.ylabel('Frequency')
    plt.title('Binomial distribution')
    plt.savefig('out.png')

**BERNOULLI DISTRIBUTION**
This is a special case of the binomial distribution where only one trial is conducted. So this time, there's no need to specify the `n` paramter. 


    from scipy.stats import bernoulli
    import matplotlib.pyplot as plt

    # generating the binomial data
    bernoulli_data = bernoulli.rvs(size=1000, p=0.8)

    # histogram plot
    plt.hist(bernoulli_data)
    plt.ylim(0, 1000)
    plt.xlabel('Number of successes')
    plt.ylabel('Frequency')
    plt.title('Bernoulli distribution')
    plt.savefig('out.png')

# probability mass/density function <a name = "12"></a>
Previously, we've been plotting the frequency of values, but what about the probability of a random variable taking on a particular value?

The **PMF (Probability Mass Function)** describes exactly that for discrete distributions. It's the probability 

For continuous distributions, we have the **PDF (Probability Density Function)**. Strictly speaking, the probability of a continuous random variable taking on a specific value is zero, since there are an infinite set of possible values. So when talking about continuous random variables we use the PDF, which describes the probability of the variable falling within some range of values.

SciPy has the `pmf` method for discrete distributions and the `pdf` method for continuous distributions.

**PMF EXAMPLE** 

    import numpy as np
    from scipy.stats import binom
    import matplotlib.pyplot as plt

    x = np.arange(0, 11)
    pmf_data = binom.pmf(x, n=10, p=0.2)
    print(pmf_data)

    plt.bar(x, pmf_data)
    plt.title('Binomial PMF')
    plt.ylabel('Probability')
    plt.savefig('out.png')

**PDF EXAMPLE**

    import numpy as np
    from scipy.stats import expon
    import matplotlib.pyplot as plt

    x = np.arange(0, 6, 0.1)
    pdf_data = expon.pdf(x)
    print(pdf_data)

    plt.plot(x, pdf_data)
    plt.title('Exponential PDF')
    plt.ylabel('Probability')
    plt.ylim(0, 1.1)
    plt.savefig('out.png')

# cumulative distribution function <a name = "13"></a>

The **Cumulative Distribution Function (CDF)** is a function between $x$ and the probability of the random variable having a value less than or equal to $x$

To calculate the CDF at different points along the distribution, we pass in a sequence (the $x$ values) to the `cdf` distribution method. What's returned are the CDF values at each of those points.

Here is an example of the `cdf` method being used for the normal distribution.


    import numpy as np
    from scipy.stats import norm
    import matplotlib.pyplot as plt

    samples = np.arange(-5.0, 5.0, 0.01)
    cdf_data = norm.cdf(samples)
    print(cdf_data)

    plt.plot(samples, cdf_data)
    plt.title('Standard Normal CDF')
    plt.ylabel('F(x) = P(X <= x)')
    plt.savefig('out.png')

By default, the `norm.cdf` will calculate the CDF for a normal distribution with a mean of 0 and standard deviation of 1. This can be changed using the `loc` and `scale` parameters, as we did with the `rvs` method.


    import numpy as np
    from scipy.stats import norm
    import matplotlib.pyplot as plt

    samples = np.arange(-5.0, 5.0, 0.01)
    cdf_data = norm.cdf(samples, loc=1, scale=0.5)
    print(cdf_data)

    plt.plot(samples, cdf_data)
    plt.title('Normal CDF mean=1, stddev=0.5')
    plt.ylabel('F(x) = P(X <= x)')
    plt.savefig('out.png')


# percentage point function <a name = "14"></a>

The **PPF (Percent-point Function)** is also known as the inverse cumulative distribution function. The function maps probability $p$ to a random variable value $x$. The probability of $p$ is the probability that a random variable takes on a value less than or equal to $x$.

Here is an example of the `ppf` method being used for the normal distribution.


    import numpy as np
    from scipy.stats import norm
    import matplotlib.pyplot as plt

    samples = np.arange(0, 1, 0.01)
    ppf_data = norm.ppf(samples)
    print(ppf_data)

    plt.plot(samples, ppf_data)
    plt.title('Normal PPF')
    plt.xlabel('Probability')
    plt.ylabel('X')
    plt.savefig('out.png')

And here is an example of the `ppf` method used for the exponential distribution.


    import numpy as np
    from scipy.stats import expon
    import matplotlib.pyplot as plt

    samples = np.arange(0, 1, 0.01)
    ppf_data = expon.ppf(samples)
    print(ppf_data)

    plt.plot(samples, ppf_data)
    plt.title('Exponential PPF')
    plt.xlabel('Probability')
    plt.ylabel('X')
    plt.savefig('out.png')
