'''
cards: a list or tuple
query: a value
return: the index the query was found at or -1 if the query was not found 
'''
def locate_card_binary(cards, query):

    # check validity of inputs
    if not(isinstance(cards, (list, tuple))) or not(isinstance(query, int)):
        raise ValueError('cards must be list or tuple and query must be int')

    # check the empty list
    if len(cards) == 0: 
        return -1

    # 2 pairs of variables to keep track of the segments and the stopping condition
    prev_left, prev_right, left, right = -1, -1, 0, len(cards) - 1

    while True: 
        # update the "prev" variables
        prev_left, prev_right = left, right

        # form the middle (floor of the midpoint)
        middle = int((left + right)/2)

        if query >= cards[middle]:
            right = middle
        else: 
            left = middle

        # stopping condition: if there was no change after the middle section code
        if (prev_left == left) and (prev_right == right):
            break

    if cards[left] == query: 
        return left
    elif cards[right] == query:
        return right
    return -1


def main():
    pass
if __name__ == '__main__':
    main()