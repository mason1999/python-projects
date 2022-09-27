### TEST FUNCTION: test_Bell
# DO NOT REMOVE ANYTHING IN THIS CELL 
# YOU CAN ADD OPTIONAL FUNCTION ARGUMENTS SAFELY 
import numpy as np

def B(n,x,poly_store = False):
    # poly_store is a flag that allows us to set the dictionary back to an empty one between invocation calls. 
    if poly_store == False:
        poly_store = {}
    if not(isinstance(x, (list, tuple, np.ndarray))):
        raise ValueError('x must be list, tuple or numpy array')
    if not(isinstance(n, int)) or n < 0:
        raise ValueError('n must be a positive integer')
    if len(x) != n:
        raise ValueError('x must have length equal to first parameter')
    # if B_n already exists then we simply return it
    if n in poly_store:
        return poly_store[n]
    # B_n doesn't exist so we recursively create it
    else:
        if n == 0: 
            poly_store[n] = 1
            return 1
        # n >= 1
        else:
            c = 0
            for i in range(n):
                v = B(i, x[0:i], poly_store = poly_store)
                c += v * x[-(i+1)]
            c *= 1/n
            poly_store[n] = c
            return c
