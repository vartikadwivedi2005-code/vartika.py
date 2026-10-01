# # Type conversion and casting in Python

# # age = input("Enter your age: ")
# # print("Your age is: " + age)

# # # string ki tarha stored hota hai. To convert it into integer, we can use int() function. For example, age = int(input("Enter your age: ")) will convert the input into integer and store it in the variable age.
# # # string ke andar string ko hi concatenate kar sakte hai. For example, "Hello, " + name + "!" will concatenate the string "Hello, ", the value of the variable name, and the string "!" together to form a new string.
# # # Type casting - Converting a variable from one type to another. For example, int() function is used to convert a string into an integer, and str() function is used to convert an integer into a string.

# # age = input("Enter your age: ")
# # new_age = int(age) # type casting
# # print(new_age)

# # print(float(new_age)) # converting integer to float
# # boolean_value = bool(new_age) # converting integer to boolean
# # print(boolean_value)

# # print(1 + 3.8) # type conversion - implicit conversion, 3.8 is converted to integer 3 and then added to 1, therefore the output is 4.8
# # print(1 + int(3.8)) #  type casting - explicit conversion, float to integer 0.8 is ignored and it is considered as only 3 therefore the output is 1+3=4

# # Sum Program => a, b => sum
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))

# sum = a + b
# print("Sum =",sum)

# #Multiplication Program => a, b => multiplication
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# multiplication = a * b
# print("Multiplication =", multiplication)

# # String creation and concatenation
name = "Tony Stark"
grade = 'A'
# print("Name:", name)
# print("Grade:", grade)

# String operations
# print(name.upper()) # converts the string to uppercase
# print(name.lower()) # converts the string to lowercase

# python strings are immutable no change in the original string is made, instead a new string is created and returned. For example, name.upper() returns a new string with all uppercase letters, but the original string name remains unchanged.

# find - 
# print(name.find("Stark")) # returns the index of the first occurrence of the substring "Stark" in the string name. If the substring is not found, it returns -1.
# # index => position python follows zero indexing.
# print(name.find('T'))

#Replace - 
# print(name.replace("Stark", "Iron Man")) # replaces the substring "Stark" with "Iron Man" in the string name. If the substring is not found, it returns the original string.

#check for presence of substring in string
print('S' in name) # returns True if the substring 'Stark' is found in the string name, otherwise returns False.
print('x' in name) # returns False if the substring 'x' is not found in the string name.

#reserved words in python are keywords that have a special meaning and cannot be used as variable names. For example, 'if', 'else', 'while', 'for', 'def', 'class', etc. are reserved words in python.

# True, False, in are reserved words in python. They are used to represent boolean values and membership testing respectively.


