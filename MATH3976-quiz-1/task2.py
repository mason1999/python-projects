### TEST FUNCTION: test_zeta_roots
# DO NOT REMOVE ANYTHING IN THIS CELL
import numpy as np
from scipy.special import gamma, digamma
from task0 import zeta
from task1 import zeta_prime


def newtons_zeta(z0):
    """ Given an initial value z0, this function finds the root of the zeta function for the set of values {z = 1/2 + ib | b in C}

    Parameters
    ----------
    t0 : real

    Returns
    -------
    root
    """
    current_approx = z0
    eps = 1e-15
    next_approx = current_approx + 10
    for i in range(50):
        next_approx = current_approx - zeta(current_approx)/zeta_prime(current_approx)
        dist = abs(next_approx - current_approx)
        if dist < eps: 
            return current_approx.imag
        elif dist > 120:
            return None
        current_approx = next_approx
    return None
def zeta_roots(a,b):
    """ Finds the non-trivial roots of the Riemann zeta function within the interval (a,b).
    
    Parameters
    ----------
    a,b : float

    Returns
    -------
    ndarray
        Sorted array of the imaginary part of non-trivial roots.
        
    """
    
    ### YOU CODE BELOW THIS LINE ###
    initial_conditions = np.arange(a, b, 0.3, dtype = float)
    t_values = np.array([]) 
    for initial in initial_conditions: 
        print(initial)
        value = newtons_zeta(0.5 + initial*1j)
        if value != None:
            t_values = np.append(t_values, value)
    
    t_values = np.sort(t_values)
    t_values = np.round(t_values, 16)
    t_values = np.unique(t_values)
    t_values = t_values[np.where(np.logical_and(t_values>=a, t_values<=b))]
    return t_values

print(zeta_roots(0, 100))

