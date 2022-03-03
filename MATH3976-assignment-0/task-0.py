### TEST FUNCTION: test_ESP
# DO NOT REMOVE ANYTHING IN THIS CELL

def ESP(k,X):
    """
        Evaluates an 
        Elementary Symmetric Polynomial of degree k.

        Parameters:
        -----------
        k int: integer degree of ESP.
        X tup: tuple of any length X = (r[0],...,r[n-1])

        The entries of X can be any real or complex numbers.

    """
    # We let n be the length of the vector X
    n = len(X)

    if n < k or k < 0: 
        return 0.0 
    if n == 1 and k == 1: 
        return X[0]
    if k == 0: 
        return 1.0
    return ESP(k, X[0:-1]) + X[-1] * ESP(k-1, X[0:-1])



### SKIP -----------------------------------------------
# This code will not be marked.

def constant_formula(a): 
    return a == 0
    
def linear_formula(a,b):
    
    if a == 0: 
        return constant_formula(b)
    if b == 0: 
        return 0.0
    
    return -b/a # single solution


def quadratic_formula(a,b,c):
    
    if a == 0: 
        return linear_formula(b,c)
    if c == 0: 
        return linear_formula(a,b), 0.0
    
    b /= -2*a
    c /= a
    
    # Now solving x**2 - 2*b*x + c = 0
    
    d = (b**2 - c)**(1/2) # (d).real >= 0 by definition.
    
    if (b).real > 0: 
        d = b + d
    else:
        d = b - d
    
    return c/d, d # two solutions 
### ----------------------------------------------

def cubic_formula(a,b,c,d):

    if a == 0: 
        return quadratic_formula(b, c, d)
    if d == 0: 
        tup = quadratic_formula(a, b, c)
        if (len(tup) == 2): 
            return 0.0, tup[0], tup[1]
        return 0.0, tup[0]

    # This is to be used later on 
    w = (-1 + 3**(1/2) * 1j)/2

    # Step 1: depress the cubic and employ a change of variables 
    # to get us a cubic polynomial in the form of y^3 + py + q = 0
    p = c/a - (b**2)/(3 * a**2)
    q = (2 * b**3)/(27 * a**3) - (b * c)/(3 * a**2) + d/a

    if p == 0: 
        y1 = (-1 * q) ** (1/3)
        y2 = y1 * w
        y3 = y2 * w
        return (y1 - b/(3*a)), (y2 - b/(3*a)), (y3 - b/(3*a))

    if q == 0: # solving the depressed cubic y^3 + py = y(y^2 + p) = 0
        tup = quadratic_formula(1, 0, p)
        if (len(tup) == 2): 
            return 0.0, tup[0], tup[1]
        return 0.0, tup[0]
        
    # Step 2: we now compare this polynomial with the identity 
    # (u + v)^3 = u^3 + 3uv(u + v) + v^3 which gets us the fact
    # that v = p/(-3u). Once we find the u and v, we find the other
    # two cube roots by multiplying by w = exp(i * 2pi/3). Then we use
    # back subsitution to find our three answers. 
    u_cubed = -q/2 + ((q/2)**2 + (p/3)**3)**(1/2)

    u1 = u_cubed**(1/3)
    v1 = p/(-3*u1)
    y1 = u1 + v1
    x1 = y1 - b/(3*a)

    u2 = u1 * w
    v2 = p/(-3 * u2)
    y2 = u2 + v2 
    x2 = y2 - b/(3*a)

    u3 = u2 * w 
    v3 = p/(-3 * u3)
    y3 = u3 + v3
    x3 = y3 - b/(3*a)
    
    return x1, x2, x3

# --------------------------------
def print_roots(tup): 
    count = 1
    for x in tup: 
        print("root " + str(count) + " is " + str(x))
        count += 1

def check_root_sup(r, coeffs): # eg (1, 1, 0, 1) = x^3 + x^2 + 0x + 1

    length = len(coeffs)
    starting_power = length - 1 
    sum = 0
    for alpha in coeffs: 
        sum += alpha * r ** starting_power 
        starting_power -= 1 
    return sum

def check_root(r, *arg): 
    list = []
    i = 0
    for x in arg: 
        list.append(x)
    tup = tuple(list)
    return check_root_sup(r, tup)

def check_roots(tup, *arg): 
    for r in tup: 
        print(check_root(r, *arg))

# coefficients 
a = 5 
b = 0
c = 0 
d = 2
# print the roots
print_roots(cubic_formula(a, b, c, d))
print("\n")
# sub the roots we get into the cubic formula
check_roots(cubic_formula(a, b, c, d), a, b, c, d)

def quartic_formula(a,b,c,d,e):
    if e == 0: # solving x(ax^3 + bx^2 + cx + d) = 0
        print("ENTERED e == 0") # TODO: delete
        tup = cubic_formula(a, b, c, d)
        if len(tup) == 1: 
            return 0.0, tup[0]
        if len(tup) == 2: 
            return 0.0, tup[0], tup[1]
        if len(tup) == 3: 
            return 0.0, tup[0], tup[1], tup[2]
    if a == 0: # solving bx^3 + cx^2 + dx + 3
        print("ENTERED a == 0") # TODO: delete
        tup = cubic_formula(b, c, d, e)
        if len(tup) == 1: 
            tup[0]
        if len(tup) == 2: 
            return tup[0], tup[1]
        if len(tup) == 3: 
            return tup[0], tup[1], tup[2]

    alph = (-3 * b**2)/(8 * a**2) + c/a 
    beta = (b**3)/(8 * a**3) - (b * c)/(2 * a**2) + d/a 
    gama = (-3 * b**4)/(256 * a**4) + (c * b**2)/(16 * a**3) - (b * d)/(4 * a**2) + e/a

    if beta == 0: 
        print("ENTERED beta == 0") # TODO: delete
        u1 = -1 * ((-1 * alph - (alph**2 - 4 * gama)**(1/2))/2)**(1/2)
        u2 = -1 * ((-1 * alph + (alph**2 - 4 * gama)**(1/2))/2)**(1/2)
        u3 = ((-1 * alph - (alph**2 - 4 * gama)**(1/2))/2)**(1/2)
        u4 = ((-1 * alph + (alph**2 - 4 * gama)**(1/2))/2)**(1/2)

        x1 = u1 - b/(4*a)
        x2 = u2 - b/(4*a)
        x3 = u3 - b/(4*a)
        x4 = u4 - b/(4*a)

        return x1, x2, x3, x4

    if gama == 0: 
        print("ENTERED gama == 0") # TODO: delete
        tup = cubic_formula(1, 0, alph, beta)
        if len(tup) == 1: 
            u1 = 0.0
            u2 = tup[0]

            x1 = u1 - b/(4*a)
            x2 = u2 - b/(4*a)
            return x1, x2
        if len(tup) == 2: 
            u1 = 0.0
            u2 = tup[0]
            u3 = tup[1]

            x1 = u1 - b/(4*a)
            x2 = u2 - b/(4*a)
            x3 = u3 - b/(4*a)
            
            return x1, x2, x3
        if len(tup) == 3: 
            u1 = 0.0
            u2 = tup[0]
            u3 = tup[1]
            u4 = tup[2]

            x1 = u1 - b/(4*a)
            x2 = u2 - b/(4*a)
            x3 = u3 - b/(4*a)
            x4 = u4 - b/(4*a)

            return x1, x2, x3, x4

    print("SOLVING MORE GENERAL QUARTIC") # TODO: delete
    # at this point we basically complete the square twice. The first time on the LHS and 
    # the second time results in us solving a necesary quadratic:
    # 8y^3 + 20alpha y^2 + (16alpha^2 - 8gamma) y + (4alpha^3 - 4alpha gamma - beta^2) = 0
    y_values = cubic_formula(8, 20 * alph, 16 * alph**2 - 8 * gama, 4 * alph**3 - 4 * alph * gama - beta**2)
    y = y_values[0]

    v1 = -1 * (3 * alph + 2 * y - (2 * beta)/((alph + 2 * y)**(1/2)))
    v2 = -1 * (3 * alph + 2 * y - (2 * beta)/((alph + 2 * y)**(1/2)))
    v3 = -1 * (3 * alph + 2 * y + (2 * beta)/((alph + 2 * y)**(1/2)))
    v4 = -1 * (3 * alph + 2 * y + (2 * beta)/((alph + 2 * y)**(1/2)))

    u1 = (-1 * ((alph + 2 * y)**(1/2)) - (v1**(1/2)))/2
    u2 = (-1 * ((alph + 2 * y)**(1/2)) + (v2**(1/2)))/2
    u3 = (((alph + 2 * y)**(1/2)) - (v3**(1/2)))/2
    u4 = (((alph + 2 * y)**(1/2)) + (v4**(1/2)))/2

    x1 = u1 - b/(4*a)
    x2 = u2 - b/(4*a)
    x3 = u3 - b/(4*a)
    x4 = u4 - b/(4*a)

    return x1, x2, x3, x4


# coefficients 
a = 1 
b = 2
c = 3 
d = 4
e = 5
# print the roots
print_roots(quartic_formula(a, b, c, d, e))
print("\n")
# sub the roots we get into the cubic formula
check_roots(quartic_formula(a, b, c, d, e), a, b, c, d, e)
