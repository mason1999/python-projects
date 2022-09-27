### TEST FUNCTION: test_quaternion_test
## DO NOT REMOVE ANYTHING IN THIS CELL ##

def quaternion_test(q): 
    
    ## INPUT YOUR CODE BELOW THIS LINE ## 
    if not (isinstance(q, tuple)):
        raise TypeError('Input is not tuple.') 

    if len(q) != 4:
        raise ValueError('Input is not length 4.')

    # all_real is True if all the types are real and false if at least one is not real
    all_real = all([isinstance(x, (int, float)) for x in q])
    if not all_real:
        raise TypeError('Element not a real number.')

    return None

def real(q):
    
     ## INPUT YOUR CODE BELOW THIS LINE ## 
    quaternion_test(q)
    
    return float(q[0])

def imag(q):
    
     ## INPUT YOUR CODE BELOW THIS LINE ## 
    quaternion_test(q)
    
    return q[1]

def jmag(q):
    
     ## INPUT YOUR CODE BELOW THIS LINE ## 
    quaternion_test(q)
    
    return q[2]

def kmag(q):
    
     ## INPUT YOUR CODE BELOW THIS LINE ## 
    quaternion_test(q)
    
    return q[3]

def string(q):

    quaternion_test(q)

    a = real(q)
    b = imag(q)
    c = jmag(q)
    d = kmag(q)

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

def add(q,r):
    
    ## INPUT YOUR CODE BELOW THIS LINE ## 
    quaternion_test(q)
    quaternion_test(r)

    q_a = real(q)
    q_b = imag(q)
    q_c = jmag(q)
    q_d = kmag(q)


    r_a = real(r)
    r_b = imag(r)
    r_c = jmag(r)
    r_d = kmag(r)
    

    return (q_a + r_a, q_b + r_b, q_c + r_c, q_d + r_d)
    

def negative(q):
    
    ## INPUT YOUR CODE BELOW THIS LINE ## 
    quaternion_test(q)

    q_a = real(q)
    q_b = imag(q)
    q_c = jmag(q)
    q_d = kmag(q)

    return (-q_a, -q_b, -q_c, -q_d)

def subtract(q,r):
    
    ## INPUT YOUR CODE BELOW THIS LINE ## 
    quaternion_test(q)
    quaternion_test(r)

    return add(q, negative(r))

def multiply(q,r):
    
    ## INPUT YOUR CODE BELOW THIS LINE ##
    quaternion_test(q)
    quaternion_test(r)

    a = real(q)
    b = imag(q)
    c = jmag(q)
    d = kmag(q)
    
    e = real(r)
    f = imag(r)
    g = jmag(r)
    h = kmag(r)

    real_part = a*e  - b*f - c*g - d*h
    i_part = a*f + b*e + c*h - d*g
    j_part = a*g - b*h + c*e + d*f 
    k_part = a*h + b*g - c*f + d*e

    return (real_part, i_part, j_part, k_part)

def conjugate(q):
    
    ## INPUT YOUR CODE BELOW THIS LINE ## 
    quaternion_test(q)
    a = real(q)
    b = imag(q)
    c = jmag(q)
    d = kmag(q)
    
    return (a, -b, -c, -d)

def absolute_value(q):
    
    ## INPUT YOUR CODE BELOW THIS LINE ## 
    quaternion_test(q)

    return (q[0]**2 + q[1]**2 + q[2]**2 + q[3]**2)**(1/2)


def inverse(q):  
    
    ## INPUT YOUR CODE BELOW THIS LINE ## 
    quaternion_test(q)
    
    a = real(q)
    b = imag(q)
    c = jmag(q)
    d = kmag(q)

    if (a == b == c == d == 0):
        raise TypeError('zero quaternion does not have an inverse')

    q_prime = conjugate(q)
    
    a = real(q_prime)
    b = imag(q_prime)
    c = jmag(q_prime)
    d = kmag(q_prime)

    norm_squared = q[0]**2 + q[1]**2 + q[2]**2 + q[3]**2

    return (a/norm_squared, b/norm_squared, c/norm_squared, d/norm_squared)


def divide(q,r):
    
    ## INPUT YOUR CODE BELOW THIS LINE ## 
    quaternion_test(q)
    quaternion_test(r)

    x = multiply(q, inverse(r))
    return x

def power(q,n):
    
    ## INPUT YOUR CODE BELOW THIS LINE ## 
    quaternion_test(q)

    ################################## TO BE DELETED ####################################
    # If float can be converted to integer, then we should accept it. 
    if isinstance(n, float): 
        if n.is_integer():
            n = int(n)
    #####################################################################################

    if not(isinstance(n, int)):
        raise ValueError('Error: input n was not an integer but must be an integer')

    # case of n == 0
    if n == 0:
        if q[0] == q[1] == q[2] == q[3] == 0:
            raise ValueError('Error: cannot perform 0**0 operation')
        # usual case: will return (1, 0, 0, 0)
        return (1, 0, 0, 0)
    # case of n == 1: return the same thing
    elif n == 1:
        return q
    # case of n >= 2: split into odd an even numbers
    elif n >= 2:
        if n % 2 == 0:
            q_power_n_on_2 = power(q, n//2)
            return multiply(q_power_n_on_2, q_power_n_on_2)
        elif n % 2 == 1:
            return multiply(power(q, n-1), q)
    else: 
        return power(inverse(q), -n)

def is_equal(q,r):
    
    ## INPUT YOUR CODE BELOW THIS LINE ## 
    quaternion_test(q)
    quaternion_test(r)
    eps = 1e-14

    # the conditons we impose
    cond_one = abs(q[0] - r[0]) < eps
    cond_two = abs(q[1] - r[1]) < eps
    cond_three = abs(q[2] - r[2]) < eps
    cond_four = abs(q[3] - r[3]) < eps
    
    # here we use the conditions
    if cond_one and cond_two and cond_three and cond_four:
        return True
    return False

def scalar(q):
    
     ## INPUT YOUR CODE BELOW THIS LINE ##
     quaternion_test(q)
     return real(q)

def vector(q):
    
     ## INPUT YOUR CODE BELOW THIS LINE ## 
    quaternion_test(q)

    b = imag(q)
    c = jmag(q)
    d = kmag(q)

    return (float(b), float(c), float(d))

def complex_pair(q):
        
    ## INPUT YOUR CODE BELOW THIS LINE ##
    quaternion_test(q)
    a = real(q)
    b = imag(q)
    c = jmag(q)
    d = kmag(q)
    return (a + b*1j, c + d*1j)

import numpy as np

def matrix(q):
    
    ## INPUT YOUR CODE BELOW THIS LINE ## 
    
    quaternion_test(q)
    a = real(q)
    b = imag(q)
    c = jmag(q)
    d = kmag(q)
    
    element_11 = a + b*1j
    element_12 = c + d*1j
    element_21 = -c + d*1j
    element_22 = a - b*1j
    return np.array([
                        [element_11, element_12],
                        [element_21, element_22]
                    ])

a = (1, 2, 3, 4)
print(matrix(a))
print(matrix(a).shape)
print(type(matrix(a)))
print(matrix(a) @ matrix(a))

