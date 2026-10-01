# Mini Project:Calculator

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /, %,**): ")

if operator == '+':
    print("The sum is:", a + b)
elif operator == '-':
    print("The difference is:", a - b)
elif operator == '*':
    print("The product is:", a * b)
elif operator == '/':
    if b != 0:
        print("The quotient is:", a / b)
    else:
        print("Error: Division by zero is not allowed.")
elif operator == '%':
    print("The remainder is:", a % b)
elif operator == '**':
    print("The result is:", a ** b)
else:
    print("Invalid operator")