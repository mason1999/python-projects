"""
This just has the functions:
    add
    sub
    mult
    div
"""

def add(x, y): 
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):  
    return x*y

def div(x, y):
    if y == 0: 
        raise ValueError('cannot divide by zero')
    return x/y

def main():
    print('hello world')
if __name__ == '__main__':
    main()