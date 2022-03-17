def samples(*numbers, **kwargs):
    num = 0 
    for x in kwargs: 
        num = kwargs[x]

    if num == 0:
        return list(numbers)
    else: 
        return list(numbers[num - 1:len(numbers):num])

if __name__ == '__main__':
    print(samples(1, 2, 3, 4, 5, 6, 7, k=2))
    print(samples(0, 1, 0, 1, 0, 1, 0, 1, 0, k=3))
    print(samples(0, 1, 0, 1, 0, 1, 0, 1, 0, k=10))
    print(samples(1, 2, 3, 4, 5, 6, 7))

    k = 2
    a = (1, 2, 3, 4, 5, 6, 7)

    print(a[k - 1:len(a):k])


