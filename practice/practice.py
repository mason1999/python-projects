def fib(n):
    """ Returns the nth Fibonacci number """
    if n == 0: 
        return 0
    if n == 1: 
        return 1
    return fib(n - 1) + fib(n - 1)

if __name__ == '__main__':
    print(fib(0))
    print(fib(1))
    print(fib(2))
    print(fib(3))
    print(fib(4))




