import numpy as np
from scipy.special import gamma, digamma
from task0 import zeta


def zeta_prime(s):
    """ Computes the 1st derivative of the Riemann zeta function in the complex plane.
    
    Parameters
    ----------
    s : array_like
        Real or complex valued argument

    Returns
    -------
    scalar or ndarray
        Values of the derivative of the Riemann zeta function
        
    """
    
    ### YOU CODE BELOW THIS LINE ###
    if isinstance(s, (int, float, complex)):
        s = complex(s)
        sigma = s.real
        t = s.imag

        if sigma == 1 and t == 0:
            # change from zeta function
            raise ValueError('cannot find derivative of zeta\'(1)')
        elif sigma < -5: # for negative numbers

            f_s = 2**s * np.pi**(s-1) * np.sin(np.pi/2 * s)
            g_s = gamma(1-s) * zeta(1-s)
            f_prime_s = (2*np.pi)**(s-1) * (np.pi * np.cos(np.pi/2 * s) + (np.log(4) + 2*np.log(np.pi)) * np.sin(np.pi/2 * s))
            g_prime_s = -digamma(1-s) * gamma(1-s) * zeta(1-s) - gamma(1-s) * zeta_prime(1-s)

            return f_prime_s * g_s + f_s * g_prime_s
        else: # the normal case
            max_eps = 1e-20
            TERM_AMOUNT = 300

            two_power_one_minus_s = 2**(1-s)

            left_term = -1 * (np.log(2)*two_power_one_minus_s)/(1-two_power_one_minus_s) * zeta(s)
            factor = 1/(1-two_power_one_minus_s)

            a_n = []
            for n in range(TERM_AMOUNT): 
                # change from zeta function
                a_n += [np.log(n+1)/((n+1)**s)]

            copied_a_n = a_n.copy()

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

            return left_term - factor * current_sum
    elif hasattr(s, "__len__"):
        vectorize_zeta_prime = np.vectorize(zeta_prime)
        s = np.array(s)
        return vectorize_zeta_prime(s)


#def zeta_prime(s):
#    """ Computes the 1st derivative of the Riemann zeta function in the complex plane.
#    
#    Parameters
#    ----------
#    s : array_like
#        Real or complex valued argument
#
#    Returns
#    -------
#    scalar or ndarray
#        Values of the derivative of the Riemann zeta function
#        
#    """
#    
#    ### YOU CODE BELOW THIS LINE ###
#    if isinstance(s, (int, float, complex)):
#        s = complex(s)
#        sigma = s.real
#        t = s.imag
#
#        if sigma == 1 and t == 0:
#            # change from zeta function
#            raise ValueError('cannot find derivative of zeta\'(1)')
#        elif sigma < -5: # for negative numbers
#            zeta_s = zeta(s)
#            ln2 = np.log(2)
#            lnpi = np.log(np.pi)
#            pi_on_2 = np.pi/2
#            zeta_1_min_s = zeta(1-s)
#
#            # change from zeta function
#            return zeta_s * (ln2 + lnpi+ pi_on_2*np.tan(pi_on_2*s) - digamma(1-s)) - zeta_s/zeta_1_min_s * zeta_prime(1-s)
#        else: # the normal case
#            max_eps = 1e-20
#            TERM_AMOUNT = 300
#
#            factor_one_minus_s = 1/(1 - 2**(1-s))
#
#            # change from zeta function
#            c = -1 * (np.log(2) * 2**(1-s))/(1-2**(1-s))
#            a_n = []
#            for n in range(TERM_AMOUNT): 
#                # change from zeta function
#                a_n += [(c-np.log(n+1))/((n+1)**s)]
#
#            copied_a_n = a_n.copy()
#
#            current_sum = 0
#            prev_sum = False
#            for n in range(TERM_AMOUNT):
#                if n == 0:
#                    current_sum += (-1)**n * copied_a_n[0]/(2**(n+1))
#                    copied_a_n = np.diff(copied_a_n)
#                else:
#                    prev_sum = current_sum
#                    current_sum += (-1)**n * copied_a_n[0]/(2**(n+1))
#                    if abs(current_sum - prev_sum) < max_eps: 
#                        print(n) # TODO delete
#                        break
#                    copied_a_n = np.diff(copied_a_n)
#
#            return factor_one_minus_s * current_sum
#    elif hasattr(s, "__len__"):
#        vectorize_zeta_prime = np.vectorize(zeta_prime)
#        s = np.array(s)
#        return vectorize_zeta_prime(s)


