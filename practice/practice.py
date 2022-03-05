from collections import Counter 
# List for our ingredients
tally = []
while True: 
    ingredient = input("Customer bought: ")
    if ingredient == '':
        break 
    tally.append(ingredient)
tally.sort()
freq_tab = Counter(tally)

if len(tally) != 0: 
    curr_name = tally[0]
    print(f"{curr_name}: {freq_tab[curr_name]}")
    for x in tally: 
        if x != curr_name: 
            curr_name = x
            print(f"{curr_name}: {freq_tab[curr_name]}")

        
