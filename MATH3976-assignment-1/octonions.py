### TEST FUNCTION: test_octonion
## DO NOT REMOVE ANYTHING IN THIS CELL ##

import numpy as np

from quaternions import quaternion

class octonion():


    """
    A class for arithmetic with octonion numbers

    Parameters (all read only)
    ----------
    .quaternion_pair       : returns the octonion as a quaternion tuple of length 2.

    Methods
    -------
    conjugate()         : returns octonion.
    _inverse()          : internal class method. 
    _unit(a)            : returns a unit of the octonions for a = 0,..., 7
    _to_octonion()      : converts int, float, complex, quaternion to octonion. class method


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
    
    def __init__(self,a=0,b=0,c=0,d=0,e=0,f=0,g=0,h=0):
        # case: all real inputs: 
        input = (a, b, c, d, e, f, g, h)
        if all([isinstance(x, (int, float)) for x in input]):
            self.___quaternion_pair = (quaternion(a, b, c, d), quaternion(e, f, g, h))
            self.___o = (a,b,c,d,e,f,g,h)
        else:
            ao = octonion._to_octonion(a)
            bo = octonion._to_octonion(b)
            co = octonion._to_octonion(c)
            do = octonion._to_octonion(d)
            eo = octonion._to_octonion(e)
            fo = octonion._to_octonion(f)
            go = octonion._to_octonion(g)
            ho = octonion._to_octonion(h)

            e0 = octonion.unit(0)
            e1 = octonion.unit(1)
            e2 = octonion.unit(2)
            e3 = octonion.unit(3)
            e4 = octonion.unit(4)
            e5 = octonion.unit(5)
            e6 = octonion.unit(6)
            e7 = octonion.unit(7)

            oct_obj = ao*e0 + bo*e1 + co*e2 + do*e3 + eo*e4 + fo*e5 + go*e6 + ho*e7
            self.___quaternion_pair = oct_obj.quaternion_pair
            self.___o = oct_obj[:]
    
        ## YOU MIGHT ADD THINGS TO __init__ ##
        
    
    
    ## HERE ARE TWO HELPFUL FUNCTION TO GET STARTED ##
    
    # self[item]
    def __getitem__(self,item):
        return self.___o[(item)]
    
    @classmethod
    def unit(self,i):
        return octonion(*(i*(0,)+(1,)+(7-i)*(0,)))
    
    
    ## PUT YOUR CODE BELOW THIS LINE ##
    
    @property
    def quaternion_pair(self):
        return self.___quaternion_pair
        
    def __str__(self):
        q1 = self.quaternion_pair[0]
        q2 = self.quaternion_pair[1]
        my_string = '(' + str(q1.real) + ',' + str(q1.imag) + ',' + str(q1.jmag) + ',' + str(q1.kmag) + ',' + str(q2.real) + ',' + str(q2.imag) + ',' + str(q2.jmag) + ',' + str(q2.kmag) + ')'
        return my_string
    
    def __repr__(self):
        return str(self)
    

    def __add__(self,other):

        q1 = self.quaternion_pair[0]
        q2 = self.quaternion_pair[1]
        
        if isinstance(other, (int, float, complex, quaternion)):
            q1 += other
        elif isinstance(other, octonion):
            r1 = other.quaternion_pair[0]
            r2 = other.quaternion_pair[1]
            q1 += r1
            q2 += r2
        elif isinstance(other, np.ndarray):
            return other + self
        return octonion(*q1[:], *q2[:])
        

    def __neg__(self):
        q1 = -self.quaternion_pair[0]
        q2 = -self.quaternion_pair[1]
        return octonion(*q1[:], *q2[:])
    
    def __sub__(self,other):
        return self + (-other)
    
    def conjugate(self):
        q1 = self.quaternion_pair[0].conjugate()
        q2 = -self.quaternion_pair[1]
        return octonion(*q1[:], *q2[:])
    
    def __mul__(self,other):
        if isinstance(other, (int, float, complex, quaternion, octonion)):
            a = self.quaternion_pair[0]
            b = self.quaternion_pair[1]
            other_oct = octonion._to_octonion(other)
            c = other_oct.quaternion_pair[0]
            d = other_oct.quaternion_pair[1]
            q1 = a*c - d.conjugate()*b
            q2 = d*a + b*c.conjugate()
            return octonion(*q1[:], *q2[:])
        elif isinstance(other, np.ndarray):
            return other.__rmul__(self)
    
    def __pow__(self,n):

        # If float can be converted to integer, then we should accept it. 
        if isinstance(n, float): 
            if n.is_integer():
                n = int(n)

        if not(isinstance(n, int)):
            raise ValueError('Error: input n was not an integer but must be an integer')

        # case of n == 0
        if n == 0:
            return octonion.unit(0)
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

    def __abs__(self):
        return ((self.conjugate() * self)[0])**(1/2)

    #def inverse(self):
    #    return 
    
    def _inverse(self):
        mod_squared = (self.conjugate() * self)[0]
        return 1/mod_squared * self.conjugate()
    
    def __truediv__(self,other):
        if isinstance(other, (int, float, complex, quaternion, octonion)):
            other_oct = octonion._to_octonion(other)
            # check the case where the zero vector was inputted. 
            if (abs(other_oct) == 0): 
                raise ZeroDivisionError()
            return self * other_oct._inverse()
        elif isinstance(other, np.ndarray):
            return self * (1/other)
    
    def __eq__(self,other):
        other_oct = octonion._to_octonion(other)
        eps = 1e-14
        q1 = self.quaternion_pair[0]
        q2 = self.quaternion_pair[1]
        r1 = other_oct.quaternion_pair[0]
        r2 = other_oct.quaternion_pair[1]

        cond1 = abs(q1[0] - r1[0]) < eps
        cond2 = abs(q1[1] - r1[1]) < eps
        cond3 = abs(q1[2] - r1[2]) < eps
        cond4 = abs(q1[3] - r1[3]) < eps

        cond5 = abs(q2[0] - r2[0]) < eps
        cond6 = abs(q2[1] - r2[1]) < eps
        cond7 = abs(q2[2] - r2[2]) < eps
        cond8 = abs(q2[3] - r2[3]) < eps

        if all([cond1, cond2, cond3, cond4, cond5, cond6, cond7, cond8]):
            return True
        return False

    def __radd__(self,other):
        return self + other
    
    def __rsub__(self,other):
        return -self + other
    
    def __rmul__(self,other):
        other_oct = octonion._to_octonion(other)
        a = other_oct.quaternion_pair[0]
        b = other_oct.quaternion_pair[1]
        c = self.quaternion_pair[0]
        d = self.quaternion_pair[1]
        q1 = a*c - d.conjugate()*b
        q2 = d*a + b*c.conjugate()
        return octonion(*q1[:], *q2[:])
    
    def __rtruediv__(self,other):
        return other * self._inverse()
    
    def __req__(self,other):
        return self == other

    @classmethod
    def _to_octonion(self, other):
        if isinstance(other, (int, float)):
            return octonion(other)
        elif isinstance(other, complex):
            return octonion(other.real, other.imag)
        elif isinstance(other, quaternion):
            return octonion(other.real, other.imag, other.jmag, other.kmag)
        elif isinstance(other, octonion):
            return other
        raise ValueError('Unable to convert to an octonian')
