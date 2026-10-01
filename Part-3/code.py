# # Arithmetic operators are used to perform mathematical operations on numbers. The basic arithmetic operators in Python are:
# # print(5 + 3) # addition
# # print(5 - 3) # subtraction
# # print(5 * 3) # multiplication
# # print(5 / 3) # division
# # print( 5 // 3) # floor division
# # # print(5 % 3) # modulo - returns the remainder of the division of 5 by 3, which is 2.
# # # print(5 ** 3) # exponentiation - returns 5 raised to the power of 3, which is 125.

# # # Assignment operators are used to assign values to variables. The basic assignment operator in Python is the equal sign (=). For example, x = 5 assigns the value 5 to the variable x. There are also compound assignment operators that combine an arithmetic operation with assignment. For example, x += 3 is equivalent to x = x + 3, and it adds 3 to the current value of x and assigns the result back to x.

# # x = 1
# # x = x + 5 
# # print(x) # prints 6
# # x += 5 # equivalent to x = x + 5
# # print(x) # prints 11
# # x = x - 5
# # print(x) # prints 6
# # x *= 5 # equivalent to x = x * 5
# # print(x) # prints 30
# # x /= 5 # equivalent to x = x / 5
# # print(x) # prints 6.0

# # i = i + 1 # equivalent to i += 1, increments the value of i by 1

# # Operator precedence determines the order in which operators are evaluated in an expression. In Python, the order of precedence is as follows (from highest to lowest):
# # 1. Parentheses ()
# # 2. Exponentiation **
# # 3. Multiplication *, Division /, Floor Division //, Modulo %
# # 4. Addition +, Subtraction -

# ans = 2 + 5 * 3
# print(ans) # prints 17, because multiplication has higher precedence than addition, so 5 * 3 is evaluated first, and then 2 is added to the result.

# ans = (2 + 5) * 3
# print(ans) # prints 21, because the parentheses have the highest precedence, so 2 + 5 is evaluated first, and then the result is multiplied by 3.

# Comparison operators are used to compare two values and return a boolean value (True or False) based on the comparison. The basic comparison operators in Python are:

# print(3 > 2) # greater than
# print(3 < 2) # less than
# print(3 == 2) # equal to
# print(3 != 2) # not equal to
# print(3 >= 2) # greater than or equal to
# print(3 <= 2) # less than or equal to
# = assignment operator and == comparison operator

# Logical operators are used to combine multiple boolean expressions and return a boolean value based on the logical operation. The basic logical operators in Python are:

# # OR - returns True if at least one of the operands is True
# STATEMENT = 3 > 5
# STATEMENT2 = 3 < 5
# print(STATEMENT or STATEMENT2) # prints True, because at least one of the operands is True.

# # AND - returns True if both operands are True
# print(STATEMENT and STATEMENT2) # prints False, because both operands are not True

# # NOT - returns True if the operand is False, and returns False if the operand is True
# # print(not STATEMENT) # prints True, because the operand is False opposite of the operand is returned.

# # # Conditional statements are used to execute a block of code based on a condition. The basic conditional statements in Python are if, elif, and else.

# age = 24
# if age >= 18:
#     print("You are an adult.")
# # indentation - proper gap between the if statement and the block of code to be executed. In Python, indentation is used to define the scope of a block of code. The standard indentation is 4 spaces. colon (:) - used to indicate the start of a block of code. In Python, a colon is used at the end of a conditional statement, loop, or function definition to indicate that the following indented block of code is part of that statement, loop, or function.

# # print("end of code") # this line is not indented, so it is not part of the if statement and will be executed regardless of the condition.

# elif age < 18:
#     print("You are a minor.")

# else:
#     print("Invalid age.")

marks = 88

if marks >= 88:
    print('A')
elif marks < 80 and marks >= 70:
    print('B')
else:
    print('C')

    
