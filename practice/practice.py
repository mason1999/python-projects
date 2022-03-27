def deleteProducts(ids, m):
    pass

if __name__ == '__main__':
    ids = [1, 1, 1, 2, 2, 3]
    set_ids = set(ids)
    # step 1: make a dictionary with the numbers as the id and the frequency as the key
    my_dic = {}
    for i in set_ids:
        my_dic[i] = 0

    print(my_dic)
    for i in ids:
        my_dic[i] = int(my_dic[i]) + 1

    print(my_dic)

