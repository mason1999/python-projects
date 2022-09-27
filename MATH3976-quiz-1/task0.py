### TEST FUNCTION: test_zeta
# DO NOT REMOVE ANYTHING IN THIS CELL

import numpy as np
from scipy.special import gamma, digamma

def zeta(s):
    """ Computes the Riemann zeta function in the complex plane.
    
    Parameters
    ----------
    s : array_like (google this if you don't know what it means.)
    Real or complex valued argument

    Returns
    -------
    scalar or ndarray
        Values of the Riemann zeta function
    
    """
    
    ### YOU CODE BELOW THIS LINE ###
    if isinstance(s, (int, float, complex)):
        s = complex(s)
        sigma = s.real
        t = s.imag

        if sigma == 1 and t == 0:
            eps = 1e-7
            return -0.5 * (gamma(0 + eps) + gamma(0 - eps))
        elif (sigma % 2 == 0 and sigma < 0 and t == 0): # case of trivial negative roots
            return 0
        elif sigma < -5: # for negative numbers
            two_power_s = 2**s
            pi_power_s_min_one = np.pi**(s-1)
            sin = np.sin(np.pi * s/2)
            gam = gamma(1-s)
            zet = zeta(1-s)

            return 2**s * np.pi**(s-1) * np.sin(np.pi * s/2) * gamma(1-s) * zeta(1-s)
        else: # the normal case
            # the following variables control the stopping conditions
            # stopping condition 1: If the difference between subsequent terms is less than this we return the values
            max_eps = 1e-20
            # stopping condition 2: note that 2**(-53) = 1.11e-16. We enforce 54 terms because differencing 53 times 
            # will leave just 1 number
            TERM_AMOUNT = 300

            # factor in front of the summation symbol
            factor_one_minus_s = 1/(1 - 2**(1-s))

            # we preprocess a list of the lag-k differences (terms 0 --> 99)
            a_n = []
            for i in range(TERM_AMOUNT): 
                a_n += [1/((i+1)**s)]

            # copy the list to work on it
            copied_a_n = a_n.copy()

            # calculate the zeta function value. 
            current_sum = 0
            prev_sum = False
            for n in range(TERM_AMOUNT):
                if n == 0:
                    current_sum += (-1)**n * copied_a_n[0]/(2**(n+1))
                    copied_a_n = np.diff(copied_a_n)
                else:
                    prev_sum = current_sum
                    current_sum += (-1)**n * copied_a_n[0]/(2**(n+1))
                    if abs(current_sum - prev_sum) < max_eps: 
                        break
                    copied_a_n = np.diff(copied_a_n)

            return factor_one_minus_s * current_sum
    elif hasattr(s, "__len__"):
        vectorize_zeta = np.vectorize(zeta)
        s = np.array(s)
        return vectorize_zeta(s)


#x = [1, 2, 3, 4]
#y = (1, )
#z = np.array(x)
#if hasattr(x, "__len__"):
#    print('x has length')
#
#if hasattr(y, "__len__"):
#    print('y has length')
#
#if hasattr(z, "__len__"):
#    print('z has length')
#
#if hasattr(1, "__len__"):
#    print('1 has length')
#
#if hasattr(1 + 1j, "__len__"):
#    print('1 + 1j has length')
#
#x = [0.1, 1, 1 + 1j]
#
#y = np.array(x)
#print(y)
