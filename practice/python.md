# Table of contents
1. [print, type and variables](#1)
2. [multiple assignment](#2)
3. [useful string methods](#3)
4. [typecasting](#4)
5. [user input](#5)
6. [string slicing](#6)
7. [if-elif-else](#7)
8. [for loop, ranges and continue](#8)
9. [Nested loops and for-else](#9)
10. [lists](#10)
11. [2D lists](#11)
12. [tuples](#12)
13. [sets](#13)
14. [dictionaries](#14)


# print, type and variables <a name="1"></a>
To print something use the `print()` function. 

The different data types we've encountered are
  
- `str` for the string class
- `int` for the int class
- `float` for the float class
- `bool` for the boolean class

To print out the type of a variable use the `type()` function. To print something out as a string, try and cast it to a string with `str(...)`

Finally to concatenate strings use the `+` operator. 

    height = 165.5
    print("type of height is " + str(type(height)))
    print("You height is " + str(height))

For `int` to increment a variable use the `+=` operator


# multiple assignment <a name="2"></a>
To assign multiple values in one line of code, use commas

    name, age, truth = "Mason", 21, True

To assign multiple values to the same value, use lots of equals

    mason1 = mason2 = mason3 = 21


# useful string methods <a name="3"></a>
To find the length of a string use the `len()` method. 

    name = "mason"
    print(len(name))
To return the index of a character in a string, use the method `.find()`

    name = "mason"
    print(name.find("p")) # prints -1
    print(name.find("m")) # prints 0

To capitalise the first letter of a string use `.capitalize()`

    name = "mason"
    print(name.capitalize()) # prints "Mason"

To convert everything to either upper case or lower case use either `.upper()` or `.lower()`

    name = "Mason"
    name1 = name.upper() # "MASON"
    name2 = name.lower() # "mason"

To check if a string contains **only digits** use the `.isdigit()` method. 

    age = "123"
    print(age.isdigit()) # prints true

    age = "123 "
    print(age.isdigit())# prints false. 

To check if a string contains **only letter** use the `.isalpha()` method. 

    name = "masonWong"
    print(name.isalpha()) # prints true

    name = "mason wong"
    print(name.isalpha()) # prints false. 

To replace all chars "i" with "o" use the `.replace()` method. 

    name = "tim tim"
    name1 = name.replace("i", "o")
    print(name1)

To concatenate strings use the `+` operator. To repeat strings use the `*` operator

    greeting = "hello"
    greeting = greeting + " world"
    greeting = greeting + " "
    greeting = greeting * 3
    print(greeting)


# typecasting <a name="4"></a>
To typecast a variable just surround the variable by the class. For example `str(var)` or `int(var)` or `float(var)` or `bool(var)`. Note that typecasting anything to a `boolean` will become true **so long as** it is not **zero** or an **empty string**. 

    z = "3"
    print(z * 3) # prints 333
    print(int(z) * 3) # prints 9
    print(float(z) * 3) # prints 9.0
    print(bool(z)) # prints true


# user input <a name = "5"></a>
To accept user input we use the `input()` function. It returns a `str` and if we also wanted a prompt we would put an optional string inside the input function `input("prompt")`

Example: 
    
      
    name = input("what is your name: ")
    age = int(input("What is your age: "))
    height = float(input("What is your height: "))
    print("Your name is " + name + " you are " + str(age) + " years old and you are " + str(height) + "cm tall.")

# String slicing <a name = "6"></a>
To split a string we can use: 
- The `[a:b]` indexing operator to obtain indices from $a \le x < b$. **note how the firs index is inclusive whereas the second index is exclusive**.  
- `slice()` function. 

An example of indexing is given below. In python, if you leave out the first index in an index (e.g `name[:6]`) python assumes you mean the `0` index. If you leave out the second index (e.g `name[6:]`) pythong assumes you mean the `last index + 1` (so the end of the string.)

    name = "mason wong"
    first_name = name[0:6] # we want indices 0 to 5. 
    first_name = name[:6] # equivalent to above
    last_name = name[6:10] #  we want indices 6 to 9
    last_name = name[6:] # equivalent to above

An example of an optional paramter in indexing is the `step`. So we can index like `[a:b:c]` where `c` is a step. 


  
    name = "mason wong"
    funky_name = name[::3] # predict: mowg <= [0, 3, 6, 9] are indices
    print(funky_name)

For the string "mason wong", negative indices are defined like so: [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1] $\iff$ [m, a, s, o, n, , w, o, n, g]


To reverse a string until the 7th index

    name = "mason wong"
    reversed_name = name[-1:(-7 - 1): -1] # start from -1, go to -7 - 1 in steps of -1

To reverse a whole string

    name = "mason wong"
    name_length = len(name)
    reversed_name = name[-1: (-1 * name_length - 1): -1]
    print(reversed_name)

Or more shorthand: 

    name = "mason wong"
    reversed_name = name[::-1]
    print(reversed_name)

The thing `a:b:c` is called a slice. In fact we can manually make a slice object

    name = "mason wong"
    print(name[2:(2+3)]) # gets "son"
    my_slice = slice(2, 2+3)
    print(name[my_slice]) # also gets "son"

Another application:

    website1 = "http://google.com"
    website2 = "http://wikipedia.com"
    my_slice = slice(7, -4)
    name1 = website1[my_slice] # gets "google"
    name2 = website2[my_slice] # gets "wikipedia"

# if-elif-else <a name = "7"></a>
The `if`, `elif` and `else` looks like:

    mark = int(input("Enter your mark: "))

    if mark >= 85:
      print("HD")
    elif mark >= 75:
      print("D")
    elif mark >= 65:
      print("CR")
    elif mark >= 50:
      print("P")
    else:
      print("F")

The comparison operators are:

- `>` : greater than
- `<` : less than 
- `>=` : greater than or equal to 
- `<=` : less than or equal to
- `==` : equal to 
- `!=` : not equal to 

The logical operators are: `and`, `or` and `not`

    m = "Magnesium"
    b = "Boronium"
    a = "Aluminium"
    c = "Copper"

    if m >= a and m <= c:
      print("alphabetically " + m + " is between") # doesn't print

    if b >= a and b <= c:
      print("alphabetically " + b + " is between") # does print

# while loop,  None and break <a name = "8"></a>
The `none` keyword is pythons version of **nothing**. 

    name = None 
    user_name = "mason"
    name = input("enter the correct name: ")
    while (name != user_name): 
      name = input("wrong name! Please enter again: ")
    print("You're right! the name was " + name)
    
We can emulate the `do-while` loop with a `True` conditional alongside a conditional `break` statement. 

    magic_number = 7
    user_number = None
    while True: 
      user_number = int(input("Enter a number: "))

      if (user_number == magic_number): 
        break;
    print("You got it! The magic number was " + str(user_number))

# for loop, ranges and continue<a name = "9"></a>
`for` loops are used to iterate over things like: `list`, `tuple`, `dictionary`, `set`, `string`, `range()`

- `range(a)` : represents the numbers  `0, 1, 2, ..., a-1`. Equivalent to `range(0, a)`
- `range(a, b)` : represents the numbers `a, a+1, ..., b-1`
- `range(a, b, c)` : represents the numbers from `a, a+1, ..., b-1` but starting at `a` then only taking the numbers that incremently add `c` to them. 

For example: 

    # a list 
    fruits = ["apple", "banana", "orange"]
    for x in fruits: 
      print(x)

    # a string 
    name = "mason wong"
    for c in name: 
      print(c)

    # a range of numbers 
    my_nums = range(0, 10)
    for i in my_nums: 
      print(i)

# Nested loops and for-else <a name = "10"></a>
An example of nested for loops can be seen here when we try to print out triangles with the following code. It can be extended to even numbers, but I'm too lazy. 

A `for-else` is of the form

    for x in (something): 
      # statments
    else: 
      # statement which always executes if for loop finishes
The `else` portion executes when the `for` loop finishes naturally. An example of it not finishing naturally is when we have a `break` statement 


    for x in range(10): 
      if (x == 9): 
        break;
      print(x)
    else: 
      print("the for loop finished naturally") # wont print # wont print
    print("the for loop finished")


Example: 

![hello](./triangle.png)



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

# lists <a name = "10"></a>
Python's version of an array, but you can have more than one variable type. To `print()` the list or elements of the list, we can use the normal `print()` function

    my_list = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding", 12, 3.14]
    print(my_list)
    print(my_list[0])
    print(my_list[1])
    print(my_list[2])
    print(my_list[3])
    print(my_list[4])
    print(my_list[5])
    print(my_list[6])

To change a variable in a list, just use the `[]` operator again. 

    my_list = ["one", "two", 3]
    my_list[2] = "three"
    print(my_list)

To append use the `.append(<val>)` method. 

To remove use the `.remove(<val>)` method.

To remove the last element use the `.pop()` method. 

To insert at an index use the `.insert(index_num, <val>)` method. 

To sort a list use the `.sort()` method. 

To clear a list use the `.clear()` method. 


  
    my_list = [4, 2, 3, 1, "d", "b", "c", "a"]
    my_list.append(5) # adds 5 to the end
    my_list.append("e") # add "e" to the end
    my_list.insert(-1, "to_be_removed") # inserts "to_be_removed" so it's now at the second last pos.
    my_list.remove("to_be_removed") # removes "to_be_removed"
    my_list.pop() # removes "e"
    my_list.clear() # empty list now. Equiv to []

To use the `.sort()` method, all the types in your list have to be the same: 

    my_ints = [8, 2, 5, 3, 1, 4, 6, 7, 10,  9]
    my_ints.sort() # sorted ascended

    my_list = ["bbb", "dd", "a", "c", "e"]
    my_list.sort() # sorted aplhanumerically

Tuples support conditionals with the `in` keyword:
    
    letters = ["a", "b", "c"]
    if "a" in letters: 
      print("first letter is in the list")

Recall that if you have a set $A = \{1,2,3,4\}$ and you also hava a set $B = \{x^2 \mid x \in A\}$ we can also write this inpyton like so: 

    A = [1, 2, 3, 4]
    B = [x**2 for x in A] # [1, 4, 9, 16]
# 2D lists <a name = "11"></a>
Basically, you can have lists as elements of lists and to access them, you need `my_list[a][b]` syntax. For example: 

    
    drinks = ["coffee", "soda", "tea"]
    dinner = ["pizza", "hamburger", "hotdog"]
    dessert = ["cake", "ice cream"]

    food = [drinks, dinner, dessert]

    print(food) # prints [['coffee', 'soda', 'tea'], ['pizza',...],...]
    print(food[2]) # prints ['cake','ice cream']
    print(food[1][0]) # prints 'pizza'
# tuples <a name = "12"></a>
tuples are ordered and **cannot change**. We can still access them with the `[]` operator. 

    student = ("mason", 21, "male")
    print(student) # ('mason', 21, 'male')
    print(student[0]) # 'mason'

tuples also support conditionals in the sense of containing a value:

    student = ("mason", 21, "male")
    if "mason" in student: 
      print("mason is present")

To count the amount of times a value appears, use the `.count(val)` method. To find the index of the first instance of a value use the `.index(val)` method
    
    my_tuple = ["a", "a", "a", "b", "b"]
    count_a = my_tuple.count("a") # returns 3
    count_b = my_tuple.count("b") # returns 2. 
    index_a = my_tuple.index("a") # returns 0 <- index of first
    index_b = my_tuple.index("b") # returns 3 <- index of first
# sets <a name = "13"></a>
To make a set use `{}` curly brackets. They are **unordered** and **unindexed**. To show unordered-ness:
    
    # run this 10 times. The order of the access will be different. 
    set = {"abcd", "cdef", "efgh", "ijkl"}
    for x in set:
        print(x)

Accessing elements in a set is much faster than a list:

    # this will print 'hello world'
    set = {"abcd", "cdef", "efgh", "ijkl"}
    if "abcd" in set: 
      print("hello world")

The methods which update the current set always return `None`. They update and that's it.

    even = {2, 4, 6, 8}
    odd = {1, 3, 5, 7}
    print(even.add(10)) # even = {2,4,6,8,10}
    print(even.remove(10)) # even = {2,4,6,8}
    print(even.clear()) # even = {}
    print(even.update(odd)) # even = {1,3,5,7}

The methds like `.union`, `.intersection`, `.difference` don't update our sets and return the sets from the math operations of $\bigcup$, $\bigcap$ and $\setminus$

    primes = {2, 3, 5, 7}
    dice = {1, 2, 3, 4, 5, 6}
    print(dice.union(primes)) # {1,2,3,4,5,6,7}
    print(dice.insersection(primes)) # {2,3,5}
    print(dice.difference(primes)) # {1,4,6}
# dictionaries <a name = "14"></a>
A dictionary is a collection of {key:value} pairs. It is similar to a set in the sense that the `keys` cannot be repeated. 

To make a dictionary 


    capitals = {'USA' : 'Washington DC',
        'India' : 'New Dehli',
        'China' : 'Beijing',
        'Russia' : 'Moscow'}
    print(capitals) # prints {'USA': 'Washington DC', 'India': 'Dehli',...}

You can update the dictionary by the `.update({key : value})` method. 


    capitals = {'USA' : 'Washington DC',
        'India' : 'New Dehli',
        'China' : 'Beijing',
        'Russia' : 'Moscow'}

    captials.update({'Germany': 'Berlin'}) # can add a new (key, value)
    capitals.update({'USA': 'Texas'}) # update the capital of USA
    print(capitals)

To get the `value` at a key use the `.get(key)` method or `my_dic[key]` indexing. The indexing is more dangerous. 

    capitals = {'USA' : 'Washington DC',
        'India' : 'New Dehli',
        'China' : 'Beijing',
        'Russia' : 'Moscow'}
    print(capitals.get('USA')) # capitals['USA'] = 'Washington DC'
    print(capitals.get('India')) # capitals['India'] = 'Dheli'
    print(capitals.get('China')) # capitals['china'] = 'Beijing'
    print(capitals.get('Russia')) # capitals['Russia'] = 'Moscow'
    print(capitals.get('Germany')) # captials['Germany'] <- throws error with this notation

To get a list of the keys that is iterable and viewable we can use the `.keys()` method

    capitals = {'USA' : 'Washington DC',
        'India' : 'New Dehli',
        'China' : 'Beijing',
        'Russia' : 'Moscow'}

    for x in capitals.keys():
      print(x)
    
To get a list of the values  that is iterable and viewable we can use the `.values()` method


    capitals = {'USA' : 'Washington DC',
        'India' : 'New Dehli',
        'China' : 'Beijing',
        'Russia' : 'Moscow'}

    for x in capitals.values():
      print(x)

To get a list of the `(key, values)` pairs we can use `.items()` method alongside the `for k, v in my_dic.items():`

    capitals = {'USA' : 'Washington DC',
        'India' : 'New Dehli',
        'China' : 'Beijing',
        'Russia' : 'Moscow'}

    for k,v in capitals.items():
      print(k, v)

