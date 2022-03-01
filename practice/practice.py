# print statements
print("I love pizza")

# variables: check type with type() function. 
## strings
first_name = "Mason"
last_name = "wong" 
hello = "hello" + " " + first_name + " " + last_name # string concatentation
print(hello)
print(type(hello)) # check type 


## ints
age = 21 # age = "21" --> age += 1 will give you a type error. 
age += 1 # same as age = age + 1
print(age)
print(type(age))
print("Your age is: " + str(age))

## floats
height = 165.5
print(height)
print(type(height))
print("Your height is " + str(height) + "cm")

## booleans
human = False
print(type(human))
print(human)
print("Are you a human: " + str(human))



name = "a b"
print( type(len(name)) )


print(name.find("p")) # returns 0 to n-1 or -1 if not found

print(name.capitalize()) # capitalises the string

print(name.upper()) # makes every character upper case

print(name.lower()) # makes every character lower case

print(name.isdigit()) # returns true if the string is only composed of digit. 

print(name.isalpha()) # returns true if the string is only composed of letters

print(name.count("f")) # counts number of "f" in the string. 

print(name.replace("e", "a")) # replaces the "e" chars with the "a" chars. 

print(name * 3)



name = "masonWong"
print(name.isalpha()) # prints true

name = "mason wong"
print(name.isalpha()) # prints false. 



name = "tim tim"
name1 = name.replace("i", "o")
print(name1)


x = 1 # int 
y = 2.0 # float 
z = "3" # a string 

print(x)
print(y)
print(z * 3)


z = "3"
print(z * 3) # prints 333
print(int(z) * 3) # prints 9
print(float(z) * 3) # prints 9.0


print(bool("3"))


name = "mason wong"
first_name = name[0:6] # we want indices 0 to 5. 
first_name = name[:6] # equivalent to above
last_name = name[6:10] #  we want indices 6 to 9
last_name = name[6:] # equivalent to above

name = "mason wong"
funky_name = name[::3] # predict: mowg <= [0, 3, 6, 9] are indices
print(funky_name)


name = "mason wong"
reversed_name = name[-1:-8:-1]
print(reversed_name)


website1 = "http://google.com"
website2 = "http://wikipedia.com"
my_slice = slice(7, -4)
name1 = website1[my_slice] # gets "google"
name2 = website2[my_slice] # gets "wikipedia"
print(name1)
print(name2)


m = "Magnesium"
b = "Boronium"
a = "Aluminium"
c = "Copper"

if m >= a and m <= c:
  print("alphabetically " + m + " is between") # doesn't print

if b >= a and b <= c:
  print("alphabetically " + b + " is between") # does print

x = None
print(x == 2)


for x in range(6):
    print(x)
print("finally done")


# 
#---- n = 1, r = 1 = floor(1/2) + 1

 #          s = 1, p = 1
###         s = 0, p = 3
#---- n = 3, r = 2 = floor(3/2) + 1


  #         s = 2, p = 1
 ###        s = 1, p = 3
#####       s = 0, p = 5
#---- n = 5, r = 3 = floor(5/2) + 1

   #        s = 3, p = 1
  ###       s = 2, p = 3
 #####      s = 1, p = 5
#######     s = 0, p = 7
#---- n = 7, r = 4 = floor(7/2) + 1


    #       s = 4, p = 1
   ###      s = 3, p = 3
  #####     s = 2, p = 5
 #######    s = 1, p = 7
#########   s = 0, p = 9
#---- n = 9, r = 5 = floor(9/2) + 1

import math # import the math module
num = 9  # the number of hashes at the bottom row
spaces = range(math.floor(num/2), -1, -1) # a range of the spaces
counter = 1 # a counter to keep track of the hashes to put
for i in spaces: # only need to index by the spaces
    # print out spaces
    for s in range(i): 
        print(" ", end = "")
    # print out hashes: we have a for loop to print hashes first
    for h in range(counter): 
        print("#", end = "")
    # always afterwards, we want to increment the counter and have a newline
    else: 
        counter += 2
        print("") # print out the newline



for x in range(10): 
  if (x == 9): 
    break;
  print(x)
else: 
  print("the for loop finished naturally") # wont print # wont print
print("the for loop finished")



drinks = ["coffee", "soda", "tea"]
if "coffee" in drinks: 
    print("blabla")


my_tuple = ["a", "a", "a", "b", "b"]
count_a = my_tuple.count("a") # returns 3
count_b = my_tuple.count("b") # returns 2. 
index_a = my_tuple.index("a")
index_b = my_tuple.index("b")
print(index_a)
print(index_b)

print("\n\n\n")

even = {2, 4, 6, 8}
odd = {1, 3, 5, 7}
print(even.add(10)) # even = {2,4,6,8,10}
print(even.remove(10)) # even = {2,4,6,8}
print(even.clear()) # even = {}
print(even.update(odd)) # even = {1,3,5,7}


print(even.union(odd)) # returns {1,2,3,4,5,6,7,8}




primes = {2, 3, 5, 7}
dice = {1, 2, 3, 4, 5, 6}
dice.clear
print(dice.union(primes))
print(dice.intersection(primes))
print(dice.difference(primes))


capitals = {'USA' : 'Washington DC',
    'India' : 'New Dehli',
    'China' : 'Beijing',
    'Russia' : 'Moscow'}
capitals.update({'Germany' : 'Berlin'})
capitals.update({'USA': 'Las Vegas'})
capitals.pop('China')

# print(capitals)
# print("\n\n\n")
# print(capitals.get('USA')) # capitals['USA']
# print(capitals.get('India')) # capitals['India']
# print(capitals.get('China')) # capitals['china']
# print(capitals.get('Russia')) # capitals['Russia']
# print(capitals.get('Germany')) # captials['Germany'] <- throws error

print(capitals.keys()) # prints the keys and not the values

x = capitals.keys()

for i in x: 
    print(i)
# print(capitals.values()) # prints the values and not the keys
# print(capitals.items()) # prints the key, value pairs

# for k,v in capitals.items():
#     print(k, v)

# for k in capitals:
#     print(k)



def r(n): 
    if n < 0: 
        return -1 
    if n == 0: 
        return 1 
    return (r(n-1) + 2)/(r(n-1)+1)
    
print(r(1))
print(r(2))
print(r(3))
print(r(4))
print(r(5))

