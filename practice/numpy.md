1. [Introduction](#1)
2. [ndarrays](#2)
3. [dtype](#3)
4. [arange, linspace](#4)
5. [ones, zeros, full, eye](#5)
6. [reshape](#6)
7. [Broadcasting](#7)
8. [operations](#8)
9. [concatenate](#9)
10. [indexing](#10)
11. [indexing II](#11)
12. [boolean masking](#12)


# Introduction
To install `numpy`

    pip3 install numpy

To import `numpy` with an alias

    import numpy as np

# ndarrays
Create ndarray from existing python sequence

    import numpy as np

    # creating a NumPy array from a list
    print(np.array([0, 1, 2, 3]))

    # creating the same NumPy array from a tuple
    print(np.array((0, 1, 2, 3)))

And we can create them from multidimensional Python sequences. Unlike lists of lists, `ndarray` rows/columns need to be the same length.

    import numpy as np

    # creating a 2D NumPy array
    a = np.array([[0, 1], [2, 3]])

    # creating a 3D NumPy array
    b = np.array([[[0, 1], [2, 3]],
                  [[4, 5], [6, 7]],
                  [[8, 9], [10, 11]]])

ndarrays have a number of `attirbutes`:

- `ndim`: Number of axes/dimensions
- `shape`: A tuple containing the sizes of each axis, in order. 
  
  - e.g for a 2D array, the shape will be `(<number of rows>, <number of columns>)`

- `size`: The number of elements of the array. 
- `dtype`: The type of the values in the array
- `itemsize`: the size of the `dtype` in bytes. 

      import numpy as np

      m = np.array([[[0, 1], [2, 3]],
                    [[4, 5], [6, 7]],
                    [[8, 9], [10, 11]]])

      print(f'ndim:     {m.ndim}')
      print(f'shape:    {m.shape}')
      print(f'size:     {m.size}')
      print(f'dtype:    {m.dtype}')
      print(f'itemsize: {m.itemsize}')

# dtype
To maximise effeciency, NumPy has its own data types for values stored inside NumPy arrays. This `dtype` is chosen by NumPy automatically when an array is created:

    import numpy as np

    x = np.array([1,2,3,4])
    print(x.dtype)

    x = np.array([0.1,0.2,0.3,0.4])
    print(x.dtype)

**INTEGER TYPES**

- `np.uint8` an unsigned integer, range: `[0, 255]`
- `np.uint16` an unsigned integer, range: `[0, 65535]`
- `np.uint32` an unsigned integer, range: `[0, 4294967295]`
- `np.uint64` an unsigned integer, range: `[0, 18446744073709551615]`
- `np.int8` signed integer, range: `[-128, 127]`
- `np.int16` signed integer, range: `[-32768, 32767]`
- `np.int32` signed integer, range: `[-2147483648, 2147483647]`
- `np.int64` signed integer, range: `[-9223372036854775808, 9223372036854775807]`

      import numpy as np

      # Notice the underflow behaviour with unsigned integers
      x = np.array([0,0,0,0], dtype=np.uint8)
      print(x.dtype)
      print(x - 1)

**FLOATING POINT TYPES**
The most relevant floating point types are: 

- `np.float32`: a smaller sized float, calculations have less precision but are faster
- `np.float64`: this is the same as the Python `float`

**BOOLEAN TYPES**
-  `np.bool`: Same as the Python `bool`

**PYTHON OBJECT TYPES**
- `object`: Allows the storing of python objects in the array

      import numpy as np

      # An ndarray of strings
      x = np.array(['a', 'b', 'c', 'd'], dtype=object)
      print(x.dtype)
      print(x + 'a')

This can be very useful:

import numpy as np

    # An ndarray of Python integers
    # This is useful because the Python integers are uncapped, and can store
    # integers of any size
    x = np.array([11], dtype=object)
    print(x.dtype)
    print(x ** 100)

    # Compare with this
    y = np.array([11], dtype=np.int64)
    print(y.dtype)
    print(y ** 100) # Notice that np.int64 has overflowed into a negative value

# arange, linspace

We can 'generate' values for an ndarray by using the `np.arange` function. The `np.arange` function is analogous to our `range` function. It accepts and interprets parameters in a similar way to `range`.

    import numpy as np

    # [0 1 2 3 4 5 6 7 8 9]
    print(np.arange(0, 10))

    # every second integer value from 0 - 9 inclusive.
    print(np.arange(0, 10, 2))

    # we can range over float values too
    print(np.arange(0, 2, 0.25))

    # and in reverse...
    print(np.arange(2, 0, -0.25))

We can use the `np.linspace` function if we have a number of elements in mind, but we don't know how spaced apart these elements should be.


    import numpy as np

    # 11 numbers evenly spaced from 0.0 to 10.0 (inclusive), 
    print(np.linspace(0, 10, 11))

    # 4 numbers evenly spaced from 0.0 to 1.0 (inclusive), 
    print(np.linspace(0, 1, 4))

The `np.linspace` function creates arrays with a `dtype` of `float` by default. We can tell it explicitly to create an array of a particular type by specifying the `dtype` parameter.


    import numpy as np

    # we can ask for other types, such as int or complex.
    print(np.linspace(0, 10, 11, dtype=int))
    print(np.linspace(0, 10, 11, dtype=complex))

# ones, zeros, full, eye

use: 

- `np.zeros((a, b))` : create a zero matrix of $a \times b$. The arg: a tuple `(a, b)`
- `np.one((a, b))` : create a ones matrix of $a \times b$. The arg: a tuple `(a, b)`
- `np.zeros(a)` : create a $1 \times a$ matrix of zeros
- `np.ones(a)` : create a $1 \times a$ matrix of ones


      import numpy as np

      # 2x3 matrix of zeros
      print(np.zeros((2, 3)))

      # 1x5 matrix of floating point ones
      print(np.ones((5,)))

      # 1x5 matrix of integer ones
      print(np.ones((5,), dtype=int))

use: 

- `np.full((a, b), x)` : to make an $a \times b$ matrix of $x$'s. 

      import numpy as np

      # 3x3 matrix of 0.25's
      print(np.full((3, 3), 0.25))

use: 

- `np.eye(a, b)` : to make an identity matrix


      import numpy as np

      print(np.eye(3, 3))
      # [[1. 0. 0.]
      #  [0. 1. 0.]
      #  [0. 0. 1.]]

      print(np.eye(3, 5))
      # [[1. 0. 0. 0. 0.]
      #  [0. 1. 0. 0. 0.]
      #  [0. 0. 1. 0. 0.]]

# reshape

We can 'reshape' an existing ndarrays into a new ndarrays with different dimensions by using the `np.reshape` function. The new dimensions are specified as a tuple.

    import numpy as np

    a = np.array([[ 0,  1,  2,  3],
                  [ 4,  5,  6,  7],
                  [ 8,  9, 10, 11]]) # a 4x3 array

    # reshape into an 2x6 array
    print(a.reshape(2, 6))

If the number of elements of the requested array doesn't match the number of elements in the original ndarray, NumPy will give us an error.

import numpy as np

    # a contains 12 elements
    a = np.array([[ 0,  1,  2,  3],
                  [ 4,  5,  6,  7],
                  [ 8,  9, 10, 11]])

    # Error!
    # ValueError: cannot reshape array of size 12 into shape (2,10)
    print(a.reshape(2, 10))

We can create a ndarray using one of the earlier functions, and then `reshape` it to our liking using the reshape function.

    import numpy as np

    print(np.arange(1, 10).reshape(3, 3))

# broadcasting
An operation between a scalar and a NumPy array is broadcasted, that is, applied element wise.


    import numpy as np

    x = np.zeros(shape=(3,3))

    # Adding a scalar value to a 2d matrix of zeros
    print(x + 5)

    # Creates 
    # [[5. 5. 5.]
    #  [5. 5. 5.]
    #  [5. 5. 5.]]


This works for the many Python operators we've seen:

    import numpy as np

    x = np.arange(4)

    print(x * 5)
    print(x % 2)
    print(x == 2)
    print(x < 3)

If two arrays have shapes are compatible, they can also be broadcasted.

    import numpy as np

    a = np.array([[ 0,  1,  2,  3],
                  [ 4,  5,  6,  7],
                  [ 8,  9, 10, 11]])

    b = np.array([10,100,1000,10000])

    print(a.shape)
    print(b.shape)

    print(a + b)
    print(a * b)
    print(a - b)

# operations
We can also apply a number of mathematical functions to our ndarray in an element-wise fashion using NumPy's universal functions. These universal functions take in our ndarray as a parameter.


    import numpy as np

    a = np.arange(1.0, 5.0).reshape(2, 2)

    print('Array a:\n', a, '\n')
    # [[1. 2.]
    #  [3. 4.]]

    print('Element-wise sin \n', np.sin(a), '\n')
    # [[ 0.84147098  0.90929743]
    #  [ 0.14112001 -0.7568025 ]]

    print('Element-wise sqrt \n', np.sqrt(a), '\n')
    # [[1.         1.41421356]
    #  [1.73205081 2.        ]]

    print('Element-wise square \n', np.square(a), '\n')
    # [[ 1.  4.]
    #  [ 9. 16.]]

    print('Element-wise exp \n', np.exp(a), '\n')
    # [[ 2.71828183  7.3890561 ]
    #  [20.08553692 54.59815003]]

There are other functions which belong to the ndarray objects are called on the array itself, these ndarray object methods. The full list of these operations can be found [here](https://numpy.org/devdocs/reference/arrays.ndarray.html#calculation``)

    import numpy as np

    a = np.arange(1, 7).reshape(2, 3)
    # [[1 2 3]
    #  [4 5 6]]

    # minimum element in the entire array
    print(a.min())
    # maximum element in the entire array
    print(a.max())
    # sum of all the elements in the array
    print(a.sum())
    # mean of all the elements
    print(a.mean())
    # standard deviation of all the elements
    print(a.std())



These methods can also take in an `axis` parameter to apply these operations for each row of a particular axis.


    import numpy as np

    a = np.arange(1, 7).reshape(2, 3)
    # [[1 2 3]
    #  [4 5 6]]

    # mean of each column [2.5 3.5 4.5]
    print(a.mean(axis=0))
    # mean of each row [2. 5.]
    print(a.mean(axis=1))

# concatenate

`concatenate()` is an easy way to join a sequence of arrays along an existing axis and its syntax is:

    numpy.concatenate((<sequence of arrays>), <axis>, <out>)

Both `<axis> (int)` and `<out> (ndarray)` are optional parameters


    import numpy as np
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6]])

    # Join a and b on axis 0
    x = np.concatenate((a, b), axis = 0)
    print(x)

    # Join a and b as a one-dimensional array
    x = np.concatenate((a, b), axis = None)
    print(x)

# indexing
There are two main ways which we can index ndarrays.

In our first way, we can index ndarrays much like we would a list of lists. Remember that ndarrays are indexed from 0, not from 1.

    import numpy as np

    a = np.array([1, 2, 3, 4])
    a[1]    # 2
    a[1:]   # [2, 3, 4]
    a[:1]   # [1]
    a[:]    # [1, 2, 3, 4]
    
    b = np.array([[1, 2],
                  [3, 4],
                  [5, 6]])
    b[1][0]     # 3
    b[1]        # [3, 4]
    b[1:]       # [[3, 4], [5, 6]]
    b[1:][1]    # [5, 6]

When we slice ndarrays, the slice references the original ndarray. That is, if we modify to our slice of the ndarray, the original ndarray will be modified too. This is not the same as Python list slices where the elements are copied.

    import numpy as np

    a = np.array([1, 2, 3, 4])

    # create a slice of a
    reference = a[0:3]
    # modify our slice
    reference[1] = 0

    print('a has been modified!', a)

# indexing II
In our second lot of examples, we show that we can also specify arrays for each dimension of the array.

Let's create an array `b`

    >>> b = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])

The following index creates the array `[1, 4, 8]`.

    >>> b[[0, 1, 2], [0, 0, 1]]
    [1, 4, 8]

How does this work? To do this, let's look at the arrays we gave as indexes: `[0, 1, 2]` and `[0, 0, 1]`.

We first look at the 0th value in each of the arrays (`0` and `0`), then the 1st value in each of the arrays (`1` and `0`), then the 2nd value in each of the arrays (`2` and `1`). Then we look up the values at those indexes respectively...


    np.array[0][0] -> 1
    np.array[1][0] -> 4
    np.array[2][1] -> 8


...and put them in an array to get our final result.

    [1, 4, 8]

# boolean masking

A powerful feature of NumPy is to isolate and select a particular subset of data using a Boolean masking operation, which tests whether an array satisfies a certain condition.

Through it, you can set a cutoff to find out which elements meet the condition.


    import numpy as np 
    b = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    mask = b > 5
    print(mask) # Check which elements satisfy the condition, b > 5

    # [[False False False]
    # [False False True]
    # [True True True]]

What's more, is that you can pick out the values that meet the cutoff. We can pass this mask to the array in the `[]` operator to apply it.


    import numpy as np
    b = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

    # Select the elements where the mask is true
    # Since it the mask is

    # [[False False False]
    #  [False False True]
    #  [True  True  True]]

    # outputs [6 7 8 9]

See how it returns all the values in positions at which the mask array is `True` in a one-dimensional array? This trick will save you a lot of time and the hassle of looping through each and every element.
print(b[b > 5])
