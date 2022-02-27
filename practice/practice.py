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

name = input("what is your name: ")
age = int(input("What is your age: "))
height = float(input("What is your height: "))

print("Your name is " + name + " you are " + str(age) + " years old and you are " + str(height) + "cm tall.")
