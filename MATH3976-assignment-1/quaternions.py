### TEST FUNCTION: test_quaternion
## DO NOT REMOVE ANYTHING IN THIS CELL ##

import numpy as np

class quaternion():


    """
    A class for arithmetic with quaternion numbers

    Parameters (all read only)
    ----------
    .real               : returns real part (0th component). 
    .imag               : returns imag part (1st component). 
    .jmag               : returns jmag part (2nd component).
    .kmag               : returns kmag part (3rd component).
    .scalar             : returns the real part as a float.
    .vector             : returns the non-real part as tuple of length 3. 
    .complex_pair       : returns the quaternion as a complex tuple of length 2.
    .matrix             : returns the quaternion as a complex 2x2 np.ndarray.

    Methods
    -------
    conjugate()         : returns quaternion.
    _inverse()          : internal class method. 
    _to_quaternion()    : converts int, float, complex or quaternion --> quaternion. class method.
    _to_complex()       : converts int, float, complex --> complex
    _unit(a)            : returns either 1, i, j or k as a quaternion for a = 0, 1, 2, 3.


    All other methods are standard magic methods:
        __str__         : str(.)
        __repr__        : for using in the interactive terminal
        __add__         : + (binary operator)
        __pos__         : + (unary operator)
        __neg__         : - (unary operator)
        __sub__         : - (binary operator)
        __mul__         : * (binary operator)
        __pow__         : ** (binary operator)
        __abs__         : abs(.)
        __truediv__     : / (binary operator)
        __eq__          : == (binary relational operator)
        __getitem__     : [] operator
    """
    
    def __init__(self,a=0,b=0,c=0,d=0):

        # check if everything is real
        q = (a, b, c, d)
        if all([isinstance(x, (int, float)) for x in q]):
            self.___real = a
            self.___imag = b
            self.___jmag = c
            self.___kmag = d
            self.___scalar = float(a)
            self.___vector = (float(b), float(c), float(d))
            self.___complex_pair = (a + b*1j, c + d*1j)
            self.___matrix = np.array([
                                          [a + b*1j, c + d*1j],
                                          [-c + d*1j, a - b*1j]
                                      ])
            self.___q = (a,b,c,d)
        elif isinstance(a, tuple) and len(a) == 2:
            z1 = quaternion._to_complex(a[0])
            z2 = quaternion._to_complex(a[1])
            a = z1.real
            b = z1.imag
            c = z2.real
            d = z2.imag
            self.___real = a
            self.___imag = b
            self.___jmag = c
            self.___kmag = d
            self.___scalar = float(a)
            self.___vector = (float(b), float(c), float(d))
            self.___complex_pair = (a + b*1j, c + d*1j)
            self.___matrix = np.array([
                                          [a + b*1j, c + d*1j],
                                          [-c + d*1j, a - b*1j]
                                      ])
            self.___q = (a,b,c,d)

        else:
            aq = quaternion._to_quaternion(a)
            bq = quaternion._to_quaternion(b)
            cq = quaternion._to_quaternion(c)
            dq = quaternion._to_quaternion(d)

            q = aq*quaternion.unit(0) + bq*quaternion.unit(1) + cq*quaternion.unit(2) + dq*quaternion.unit(3)

            self.___real = q.real
            self.___imag = q.imag
            self.___jmag = q.jmag 
            self.___kmag = q.kmag 
            self.___scalar = float(q.real)
            self.___vector = (float(q.imag), float(q.jmag), float(q.kmag))
            self.___complex_pair = (q.real + q.imag*1j, q.jmag + q.kmag*1j)
            self.___matrix = np.array([
                                          [q.real + q.imag*1j, q.jmag + q.kmag*1j],
                                          [q.jmag + q.kmag*1j, q.real - q.imag*1j]
                                      ])
            self.___q = (q.real, q.imag, q.jmag, q.kmag)

        ## YOU MIGHT ADD THINGS TO __init__ ##

    ## HERE ARE TWO HELPFUL FUNCTION TO GET STARTED ##
    
    # self[item]
    def __getitem__(self,item):
        return self.___q[(item)]
    
    @classmethod
    def unit(self,i):
        return quaternion(*(i*(0,)+(1,)+(3-i)*(0,)))
    
    
    ## PUT YOUR CODE BELOW THIS LINE ##
    
    # self.real
    @property
    def real(self):
        return self.___real
    
    # self.imag
    @property
    def imag(self):
        return self.___imag
    
    # self.jmag
    @property
    def jmag(self):
        return self.___jmag
    
    # self.kmag
    @property
    def kmag(self):
        return self.___kmag
    
    # self.scalar
    @property
    def scalar(self):
        return float(self.___scalar)
    
    # self.vector
    @property
    def vector(self):
        return (float(self.___imag), float(self.___jmag), float(self.___kmag))
    
    # self.complex_pair
    @property
    def complex_pair(self):
        return (self.real + self.imag * 1j, self.jmag + self.kmag * 1j)
    
    # self.matrix
    @property
    def matrix(self):
        return np.array([
                            [self.real + self.imag * 1j, self.jmag + self.kmag * 1j],
                            [-self.jmag + self.kmag * 1j, self.real - self.imag * 1j]
                        ])
    
    # str(self)
    def __str__(self):
        a = self.real
        b = self.imag
        c = self.jmag
        d = self.kmag

        # The string to be formed
        my_str = '('


        if a != 0:
            # string versions of a, b, c, d
            a_str = str(a)
            b_str = '+' + str(b) + 'i' if b >= 0 else str(b) + 'i'
            c_str = '+' + str(c) + 'j' if c >= 0 else str(c) + 'j'
            d_str = '+' + str(d) + 'k' if d >= 0 else str(d) + 'k'

            my_str += a_str + b_str + c_str + d_str + ')'
            return my_str 

        b_str = str(b) + 'i'
        c_str = '+' + str(c) + 'j' if c >= 0 else str(c) + 'j'
        d_str = '+' + str(d) + 'k' if d >= 0 else str(d) + 'k'

        my_str += b_str + c_str + d_str + ')'
        return my_str
    
    # self
    def __repr__(self):
        return str(self)

    # self + other
    def __add__(self,other):
        if isinstance(other, (int, float)):
            a = self.real + other
            b = self.imag
            c = self.jmag
            d = self.kmag
            return quaternion(a, b, c, d)

        elif isinstance(other, complex):
            a = self.real + other.real
            b = self.imag + other.imag
            c = self.jmag
            d = self.kmag
            return quaternion(a, b, c, d)

        elif isinstance(other, quaternion):
            a = self.real + other.real
            b = self.imag + other.imag
            c = self.jmag + other.jmag
            d = self.kmag + other.kmag
            return quaternion(a, b, c, d)

        elif isinstance(other, np.ndarray):
            return other + self
        return NotImplemented
    
    # +self
    def __pos__(self):
        return self
    
    # -self
    def __neg__(self):
        return -1 * self
    
    # self.conjugate()
    def conjugate(self):
        a = self.real
        b = self.imag
        c = self.jmag
        d = self.kmag
        return quaternion(a, -b, -c, -d)
    
    # self - other
    def __sub__(self,other):
        return self + (-other)
    
    # self*other
    def __mul__(self,other):
        a = self.real
        b = self.imag
        c = self.jmag
        d = self.kmag

        if isinstance(other, (int, float)):
            return quaternion(a*other, b*other, c*other, d*other)
        elif isinstance(other, complex):
            e = other.real
            f = other.imag
            real_part = a*e - b*f
            imag_part = b*e + a*f
            jmag_part = c*e + d*f
            kmag_part = d*e - c*f
            return quaternion(real_part, imag_part, jmag_part, kmag_part)
        elif isinstance(other, quaternion):
            e = other.real
            f = other.imag
            g = other.jmag 
            h = other.kmag
            real_part = a*e - b*f - c*g - d*h
            imag_part = a*f + b*e + c*h - d*g
            jmag_part = a*g - b*h + c*e + d*f
            kmag_part = a*h + b*g - c*f + d*e
            return quaternion(real_part, imag_part, jmag_part, kmag_part)

        elif isinstance(other, np.ndarray):
            return other.__rmul__(self)
        return NotImplemented
    
    # self._inverse()
    def _inverse(self):
        a = self.real
        b = self.imag
        c = self.jmag
        d = self.kmag
        norm_squared = a**2 + b**2 + c**2 + d**2

        if norm_squared == 0:
            raise ZeroDivisionError() 

        return 1/norm_squared * self.conjugate()
    
    # self**n
    def __pow__(self,n):

        # If float can be converted to integer, then we should accept it. 
        if isinstance(n, float): 
            if n.is_integer():
                n = int(n)

        if not(isinstance(n, int)):
            raise ValueError('Error: input n was not an integer but must be an integer')

        # case of n == 0
        if n == 0:
            return quaternion(1, 0, 0, 0)
        # case of n == 1: return the same thing
        elif n == 1:
            return self 
        # case of n >= 2: split into odd an even numbers
        elif n >= 2:
            if n % 2 == 0:
                q_power_n_on_2 = self**(n//2)
                return q_power_n_on_2 * q_power_n_on_2
            elif n % 2 == 1:
                return self**(n-1) * self
        else: 
            return (1/self)**(-n)
    
    # abs(self)
    def __abs__(self):

        a = self.real
        b = self.imag
        c = self.jmag
        d = self.kmag

        return (a**2 + b**2 + c**2 + d**2)**(0.5)
    
    # TODO
    # self/other
    def __truediv__(self,other):
        if isinstance(other, (int, float, complex)):
            return self * other**(-1)
        elif isinstance(other, quaternion):
            return self * other._inverse()
        elif isinstance(other, np.ndarray):
            return self * (1/other)
        else:
            return NotImplemented
            
    
    # self == other
    def __eq__(self,other):
        eps = 1e-15
        if abs(self - other) < eps: 
            return True
        return False
    
    # other + self
    def __radd__(self,other):
        return self + other
    
    # other - self
    def __rsub__(self,other):
        return -self + other
    
    # other*self
    def __rmul__(self,other):
        a = self.real
        b = self.imag
        c = self.jmag
        d = self.kmag

        if isinstance(other, (int, float)):
            return quaternion(a*other, b*other, c*other, d*other)
        elif isinstance(other, complex):
            e = other.real
            f = other.imag
            real_part = a*e - b*f
            imag_part = b*e + a*f
            jmag_part = c*e - d*f
            kmag_part = d*e + c*f
            return quaternion(real_part, imag_part, jmag_part, kmag_part)
        return 
    
    # other/self
    def __rtruediv__(self,other):
        return other * self._inverse()
    
    # other == self
    def __req__(self,other):
        return self == other

    # class method which converts the input to a quaternion. 
    @classmethod
    def _to_quaternion(self, other):
        if isinstance(other, (int, float)):
            return quaternion(other)
        elif isinstance(other, complex):
            return quaternion(other.real, other.imag)
        elif isinstance(other, quaternion):
            return other
        return 

    # class method which converts the input to a complex. 
    @classmethod
    def _to_complex(self, other):
        if isinstance(other, (int, float)):
            return complex(other)
        elif isinstance(other, complex):
            return other
        return 

x = quaternion(1, 2, 3, 4)
y = quaternion(0, -2, 3, -4)
one = quaternion(1, 0, 0, 0)
i = quaternion(0, 1, 0, 0)
j = quaternion(0, 0, 1, 0)
k = quaternion(0, 0, 0, 1)
dec = quaternion(-1.1, -2.2, -3.3, 4.4)
