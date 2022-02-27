# Table of contents
1. [print, type and variables](#1)
2. [multiple assignment](#2)
3. [useful string methods](#3)
4. [typecasting](#4)
5. [user input](#5)

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
