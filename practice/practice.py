import sys 

n = int(sys.argv[1])

i = 1
while n >= 1: 
    print(" " * (n - 1), end = "")
    stars = "*" * i
    print(stars)
    n -= 1
    i += 2
