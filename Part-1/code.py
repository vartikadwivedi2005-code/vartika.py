print("Hello, World!","Vartika")

print("Vartika")


# python is a case sensitive language. For example, the variable name "print" is different from "Print".

# Variable - A container for storing data values.
# variable name and variable value are separated by an equal sign (=). For example, x = 5 assigns the integer value 5 to the variable x.
# and name ="Vartika" name is a variable name and "Vartika" is the variable value.

name = "Vartika"
print(name)
age = 20
print(age)

# print("name") will print the string "name" and not the value of the variable name. To print the value of the variable name, you need to remove the quotes.

# values change then the old value is overwritten and new values are assigned to the variable. For example, if you assign a new value to the variable name, the old value will be overwritten and the new value will be assigned to the variable name.

# no need to write type of variable while declaring a variable. Python is a dynamically typed language, which means that you don't need to specify the type of a variable when you declare it. The type of a variable is determined at runtime based on the value assigned to it.

print(type(name)) # <class 'str'>
print(type(age)) # <class 'int'>
# types of variables in python are:
# 1. int - Integer
# 2. float - Floating point number
# 3. str - String
# 4. bool - Boolean
# 5. list - List

cgpa = 9.5
isStudent = True
print(type(cgpa)) # <class 'float'>
print(type(isStudent)) # <class 'bool'>

# user input() function is used to take input import string from the user. The input() function takes a string as an argument, which is displayed as a prompt to the user. The input() function returns the input as a string.
input("Enter your name: ")
name = input("Enter your name: ")
print("Hello, " + name + "!")  #concatanation

# concatenation - Joining two or more strings together. For example, "Hello, " + name + "!" joins the string "Hello, ", the value of the variable name, and the string "!" together to form a new string.

# comments - Lines that are ignored by the Python interpreter. They are used to explain the code and make it more readable.
# Learning how to take input in Python


# python code.py to run in terminal