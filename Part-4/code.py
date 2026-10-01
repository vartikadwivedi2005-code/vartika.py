# # Range - Generate a sequence of numbers
# # range(5) - {0, 1, 2, 3, 4}

# nums = range(5)
# print(nums) # prints range(0, 5), which is a range object that represents the sequence of numbers from 0 to 4.

# range(5, 10) # {5, 6, 7, 8, 9}
# # range(start, stop, step) - generates a sequence of numbers starting from start (inclusive) to stop (exclusive) with a step size of step. For example, range(0, 10, 2) will generate the sequence {0, 2, 4, 6, 8}.

# range(0, 10, 2) # {0, 2, 4, 6, 8}

# loops => repeat 
# # While loop - executes a block of code repeatedly as long as a condition is true. For example, while True: will execute the block of code indefinitely until a break statement is encountered.

# # counter = 0 l 2 3 4 5  counter =i
# i = 0
# while i <= 5:  # infinite loop - executes the block of code indefinitely until a break statement is encountered. The condition i <= 5 is always true, so the loop will run forever.
#     print("Hello, World!") # this line will be executed repeatedly as long as the condition is true.
#     i += 1
# print("end of code")

# command + c to stop the infinite loop in terminal. It will raise a KeyboardInterrupt error and stop the execution of the program.

# i = 1
# while i <= 5:
    # print(i * "*") # prints a triangle pattern of asterisks. The number of asterisks printed in each line is equal to the value of i, which increases by 1 in each iteration of the loop.
    # i += 1
    # * for concatenation, it will concatenate the string "*" with itself i times and print the result. For example, when i = 3, it will print "***".

# i = 5
# while i > 0:
#     print(i * "*")
#     i -= 1 # decreasing triangle

#For loop - executes a block of code for a fixed number of iterations. For example, for i in range(5): will execute the block of code 5 times, with the variable i taking on the values 0, 1, 2, 3, and 4 in each iteration.


# nums = range(5)
# for i in range(5): # for loop - executes a block of code for a fixed number of iterations. The loop will run 5 times, with i taking on the values 0, 1, 2, 3, and 4 in each iteration.
    # print(i) # prints the value of i in each iteration of the loop. The loop will run 5 times, with i taking on the values 0, 1, 2, 3, and 4 in each iteration.

#1 - 5
# for i in range(1,6):
#     print(i)

# 1 - 10 => even numbers
# for i in range(1,11):
#     if(i % 2 == 0):
#         print(i)
    
# for i in range(1,11,2):
    # print(i)

# multiples of 3 
for i  in range(1,31):
    if(i == 2):
        continue # continue statement - used to skip the current iteration of the loop and move on to the next iteration.
    if (i % 3 == 0):
        print(i)
print("out of loop")
#break statement - used to exit the loop prematurely, before the loop condition is false. For example, if i == 2: break will exit the loop when i is equal to 2, and the program will continue executing the code after the loop.
