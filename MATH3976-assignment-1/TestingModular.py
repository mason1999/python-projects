def is_prime(p):
    
    ## INPUT YOUR CODE BELOW THIS LINE ## 
    if isinstance(p, float): 
        if p.is_integer():
            p = int(p)

    if not(isinstance(p, int)):
        raise ValueError('Error: input p was not an integer but must be an integer')

    n = abs(p)
    if n == 0: return False
    
    # implementation was obtained from wikipedida: https://en.wikipedia.org/wiki/Primality_test
    if n == 0 or n == 1:
        return False
    elif n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i**2 <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

def add(a,b,p): 
    
    ## INPUT YOUR CODE BELOW THIS LINE ## 
    ###################################### check types of a, b and p ####################
    if isinstance(a, float):
        if a.is_integer():
            a = int(a)
    if not(isinstance(a, int)):
        raise ValueError('Error: input a was not an integer but must be an integer')
    if isinstance(b, float):
        if b.is_integer():
            b = int(b)
    if not(isinstance(b, int)):
        raise ValueError('Error: input b was not an integer but must be an integer')
    if isinstance(p, float):
        if p.is_integer():
            p = int(p)
    if not(isinstance(p, int)):
        raise ValueError('Error: input p was not an integer but must be an integer')
    if p <= 0: 
        raise ValueError('Error: input p must be a positive number')
    ######################################################################################
    c = a%p
    d = b%p
    return (c+d)%p

def subtract(a,b,p):
    
    ## INPUT YOUR CODE BELOW THIS LINE ## 
    ###################################### check types of a, b and p ####################
    if isinstance(a, float):
        if a.is_integer():
            a = int(a)
    if not(isinstance(a, int)):
        raise ValueError('Error: input a was not an integer but must be an integer')
    if isinstance(b, float):
        if b.is_integer():
            b = int(b)
    if not(isinstance(b, int)):
        raise ValueError('Error: input b was not an integer but must be an integer')
    if isinstance(p, float):
        if p.is_integer():
            p = int(p)
    if not(isinstance(p, int)):
        raise ValueError('Error: input p was not an integer but must be an integer')
    if p <= 0: 
        raise ValueError('Error: input p must be a positive number')
    ######################################################################################
    c = a%p
    d = b%p
    return (c-d)%p

def multiply(a,b,p):
    
    ## INPUT YOUR CODE BELOW THIS LINE ## 
    ###################################### check types of a, b and p ####################
    if isinstance(a, float):
        if a.is_integer():
            a = int(a)
    if not(isinstance(a, int)):
        raise ValueError('Error: input a was not an integer but must be an integer')
    if isinstance(b, float):
        if b.is_integer():
            b = int(b)
    if not(isinstance(b, int)):
        raise ValueError('Error: input b was not an integer but must be an integer')
    if isinstance(p, float):
        if p.is_integer():
            p = int(p)
    if not(isinstance(p, int)):
        raise ValueError('Error: input p was not an integer but must be an integer')
    if p <= 0: 
        raise ValueError('Error: input p must be a positive number')
    ######################################################################################
    c = a%p
    d = b%p
    return (c*d)%p

def inverse(a,p):
    
    ## INPUT YOUR CODE BELOW THIS LINE ## 
    if not(is_prime(p)):
        raise ValueError('p must be a prime number')

    if a == 0: 
        raise ValueError('a must be a non zero integer')

    if p <= 0: 
        raise ValueError('p must be positive')

    # convert a = a (mod p) and p = abs(p)
    a = a % p

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
    
    return t

def test_inverse(p):
    for i in range(1, p):
        print("The inverse of {} is {}".format(i, inverse(i, p)))

def divide(a,b,p):
    
    ## INPUT YOUR CODE BELOW THIS LINE ## 
    if not(is_prime(p)):
        raise ValueError('p must be a prime number')

    if a == 0: 
        raise ValueError('a must be a non zero integer')

    if p <= 0: 
        raise ValueError('p must be positive')

    a = a%p
    b = b%p
    c = inverse(a, p) * b

    return c%p

def power(a,k,p):
    
    ## INPUT YOUR CODE BELOW THIS LINE ## 

    # If float can be converted to integer, then we should accept it. 
    if isinstance(k, float): 
        if k.is_integer():
            k = int(k)

    if not(isinstance(k, int)):
        raise ValueError('Error: input k was not an integer but must be an integer')

    a = a % p

    if k == 0: 
        return 1 % p

    elif k == 1:
        return a
    elif  k >= 2:
        if k % 2 == 0:
            a_power_k_on_2 = power(a, k//2, p) % p
            return (a_power_k_on_2 * a_power_k_on_2)%p
        elif k % 2 == 1:
            return (power(a, k-1, p) * a)%p
    else:
        a_inv = inverse(a, p) 
        return power(a_inv,-k, p) % p 

def absolute(a,p):
    
    ## INPUT YOUR CODE BELOW THIS LINE ## 
    a = a%p
    if p - a > a: 
        return a
    else:
        return p - a
