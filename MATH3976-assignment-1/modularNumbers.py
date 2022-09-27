### TEST FUNCTION: test_Mod
# DO NOT REMOVE ANYTHING IN THIS CELL

import numpy as np

class Mod:
    """
    A class to compute arithmetic (+,-,*,/,**,abs) with the Integers Mod Prime. 
    
    Parameters
    ----------
    n : Integer
    p : Prime Integer 
    
    Methods
    -------
    __init__    : constructor
    __call__    : Treats a instance like a function and can use this to return other mod objects of the same length
    __int__     : Discards the length and returns the number itself as an int
    __len__     : Discards the number and returns the prime as an int
    __float__   : Discards the length and returns the number as a float
    __str__     : Returns 'num % prime'
    __repr__    : 
    """
    
    ## DO NOT ALTER __init__ ##
    
    # self = Mod(n,p) or Mod(p)
    def __init__(self,*args):
        
        if len(args) == 0:
            raise ValueError('p undefined.')
        if len(args) == 1:
            if isinstance(args[0],Mod):
                n,p = int(args[0]), len(args[0])
            else:
                n,p = 0, int(args[0])
        if len(args) == 2: 
            n,p = int(args[0]), int(args[1])
            
        if not self.is_prime(p): 
            raise ValueError('p must be prime.')
        
        self.p = p
        self.n = n % p
    
    ## HERE ARE A FEW FREE EXAMPLES ##
    
    # self(n):
    def __call__(self,n): 
        return Mod(int(n),self.p)
    
    # int(self)
    def __int__(self): 
        return int(self.n)
    
    # len(self)
    def __len__(self): 
        return self.p
    
    # float(self)
    def __float__(self): 
        return float(int(self.n))
        
    # str(self)
    def __str__(self): 
        n, p = int(self), str(len(self))
        return f'{n:{len(p)}} % ' + p
    
    def __repr__(self):
        n, p = int(self), str(len(self))
        return f'{n:{len(p)}}'
    
    
    ## NOW IT'S YOUR TURN ##
    
    # self.is_prime(p)
    def is_prime(self,p):
        if isinstance(p, float): 
            if p.is_integer():
                p = int(p)

        if not(isinstance(p, int)):
            raise ValueError('Error: input n was not an integer but must be an integer')

        #n = abs(p) TODO
        if p < 0: return False
        if p == 0: return False
        
        # implementation was obtained from wikipedida: https://en.wikipedia.org/wiki/Primality_test
        if p == 0 or p == 1:
            return False
        elif p == 2 or p == 3:
            return True

        if p % 2 == 0 or p % 3 == 0:
            return False

        i = 5
        while i**2 <= p:
            if p % i == 0 or p % (i+2) == 0:
                return False
            i += 6
        return True
    
    # self + other
    def __add__(self,other):
        p = self.p
        a = self.n % p

        if isinstance(other, int):
            other = other % p
            return Mod((a+other)%p, p)
        elif isinstance(other, Mod):
            q = other.p
            b = other.n % q
            if p != q:
                raise ValueError('cannot add as prime numbers are not the same')
            c = (a+b)%p
            return Mod(c, p)
        elif isinstance(other, np.ndarray):
            return other + self
        raise ValueError('Error: second operand was not an int, Mod or numpy array')
        return NotImplemented

    # self - other
    def __sub__(self,other):
        return self + (-other)
    
    # -self
    def __neg__(self): 
        return -1 * Mod(self)
    
    # abs(self)
    def __abs__(self):     
        p = self.p
        a = self.n % p
        if p - a > a: 
            return a
        else:
            return p - a
        return NotImplemented
    
    # self * other
    def __mul__(self,other):
        p = self.p
        a = self.n % p

        if isinstance(other, int):
            other = other % p
            c = (a*other)%p
            return Mod(c, p)
        elif isinstance(other, Mod):
            q = other.p
            b = other.n % q
            if p != q:
                raise ValueError('cannot multiply as prime numbers are not the same')
            c = (a*b)%p
            return Mod(c, p)
        elif isinstance(other, np.ndarray):
            return other * self
        raise ValueError('Error: second operand was not an int, Mod or numpy array')
        return NotImplemented
    
    # self**n
    def __pow__(self,n):
        p = self.p
        a = self.n % p

        # If float can be converted to integer, then we should accept it. 
        if isinstance(n, float): 
            if n.is_integer():
                n = int(n)

        if not(isinstance(n, int)):
            raise ValueError('Error: input n was not an integer but must be an integer')

        if n == 0: 
            return Mod(1, p)
        elif n == 1:
            return Mod(a, p)
        elif  n >= 2:
            if n % 2 == 0:
                power_n_on_2 = Mod(a, p)**(n//2)
                return power_n_on_2 * power_n_on_2
            elif n % 2 == 1:
                power_n_minus_1 = Mod(a, p)**(n-1)
                power_1 = Mod(a, p)
                return power_n_minus_1 * power_1
        else:
            return self.inverse()**(-n)
        return NotImplemented
        
        
    # self / other TODO. Remember to take care of the case where n is a mulitiple of p. 
    def __truediv__(self,other):
        p = self.p
        a = self.n % p

        if isinstance(other, int):
            other = other % p
            if other == 0:
                raise ZeroDivisionError()
            other = Mod(other, p)
        if isinstance(other, Mod):
            return self * other.inverse()
        elif isinstance(other, np.ndarray):
            return 1/other * self
        else:
            return NotImplemented
    
    # self.inverse()
    def inverse(self):
        p = self.p 
        a = self.n % p

        if a == 0: 
            raise ZeroDivisionError()

        # initial condition: we know that p > a 
        r_prev = p 
        s_prev = 1
        t_prev = 0

        r_curr = a
        s_curr = 0
        t_curr = 1

        while True:
            q_next = int(r_prev//r_curr)
            r_next = r_prev % r_curr
            s_next = s_prev - q_next*s_curr
            t_next = t_prev - q_next*t_curr

            if r_next == 0:
                break

            r_prev = r_curr
            s_prev = s_curr
            t_prev = t_curr

            r_curr = r_next
            s_curr = s_next
            t_curr = t_next

        t = t_curr % p
        return Mod(t, p)
    
    # self == other
    def __eq__(self,other): 
        p = self.p
        a = self.n % p

        if isinstance(other, int):
            other = other % p
            if other == a: 
                return True
        elif isinstance(other, Mod):
            q = other.p
            b = other.n % q
            if q == p and a == b:
                return True
        return False
    
    # self != other
    def __ne__(self,other):
        return not(self == other)
    
    # other + self
    def __radd__(self, other): 
        return self + other
    
    # other - self
    def __rsub__(self,other): 
        return (-self) + other
    
    # other * self
    def __rmul__(self, other):
        return self * other
    
    # other / self
    def __rtruediv__(self,other):
        return other * self.inverse()

    # added myself
    def __req__(self, other):
        return self == other
    # added myself
    def __rneq__(self, other):
        return self != other
