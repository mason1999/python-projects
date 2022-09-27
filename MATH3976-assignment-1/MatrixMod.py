### TEST FUNCTION: test_MatrixMod
# DO NOT REMOVE ANYTHING IN THIS CELL

import numpy as np

from task3 import Mod


def B(n,x,poly_store = False):
    if poly_store == False:
        poly_store = {}
    if not(isinstance(x, (list, tuple, np.ndarray))):
        raise ValueError('x must be list, tuple or numpy array')
    if not(isinstance(n, int)) or n < 0:
        raise ValueError('n must be a positive integer')
    if len(x) != n:
        raise ValueError('x must have length equal to first parameter')
    if n in poly_store:
        return poly_store[n]
    else:
        if n == 0: 
            poly_store[n] = 1
            return 1
        else:
            c = 0
            for i in range(n):
                v = B(i, x[0:i], poly_store = poly_store)
                c += v * x[-(i+1)]
            c = c/n
            poly_store[n] = c
            return c

class MatrixMod(np.ndarray):
    """An inherited class of numpy.ndarray that handles Mod(p) numbers a bit better.
    
    Warnings:
        This has not been tested extensively. 
        Arrays might not behave properly when casting to other types.
        
        The .inverse() and .det() methods only work for len(array) < p.
        
        Parameters
        ----------
        array: np.ndarray
        p    : int (prime)
        
        
        Methods
        -------
        .inverse() computes inverse of square array with len < p
        .det()     computes determinant of square array with len < p
        
    """
    
    def __new__(cls,array,p):        
        obj   = np.asarray(array).view(cls)
        obj.p = p
        return obj + Mod(p)
    
    def __array_finalize__(self, obj):
        if obj is None: return
        self.p = getattr(obj, 'p', None)
    
    def __str__(self):
        return np.ndarray.__str__(self) + f' % {self.p}'
    
    def __repr__(self):
        return np.ndarray.__repr__(self)[:-13] + f'{self.p})'
    
    ## PUT YOUR CODE BELOW THIS LINE ##
    ## YOU CAN ADD OPTIONAL FUNCTION ARGUMENTS SAFELY ###
    
    def inverse(self):
        n = len(self) 
        p = self.p
        if p <= n:
            return NotImplemented
        # Step 1: compute the matrix power of I, A, A^2, A^3, ..., A^n and store them in a dictionary. 
        # Also store the trace of the matrices into a list representing [x0, x1, ..., x_{n-1}]
        # Also prepare a dictionary to store the bell polynomials we will use
        matrix_powers = {}
        input_arguments = []
        bell_polynomials = {}
        for i in range(0, n+1):
            if i == 0:
                matrix_powers[i] = MatrixMod(np.eye(n, dtype=int), p)
            elif i == 1:
                matrix_powers[i] = self
                input_arguments += [-matrix_powers[i].trace()]
            else: 
                matrix_powers[i] = matrix_powers[i-1] @ self
                input_arguments += [-matrix_powers[i].trace()]

        # Step 2: compute the determinant and in the same step, you should have stored the bell polynomials
        # from B0, B1, B2, ..., Bn
        det = self.det(input_arguments, bell_polynomials)

        # Step 3: compute the inverse by:
        # (1) calculating the sum of the powers of the matrices scaled by the bell polynomials
        # (2) multiplying by (-1)**(n+1)/determinant
        c = 0
        for i in range(n):
            c = c + bell_polynomials[i] * matrix_powers[n - (i+1)]
        scaling_factor = (-1)**(n+1)/det
        c = c * scaling_factor
        return c
    
    def det(self, input_arguments, poly_store = False):
        if poly_store == False:
            poly_store = {}
        n = len(self)
        # we should have a lingering reference to our dictionary
        return (-1)**n * B(n, input_arguments, poly_store)

    
n = 20 
p = 29
A = MatrixMod(np.random.randint(-p,p,(n,n)),p)

print('A is')
print(A, '\n')
print('A inverse is')
print(A.inverse(), '\n')
print('This should give us the identity')
print(A@A.inverse(), '\n')
# This should give an identity matrix, or an error if the determinant vanishes.
#A.inverse() @ A
