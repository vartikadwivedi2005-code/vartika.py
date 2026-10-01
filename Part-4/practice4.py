# # Odd numbers from 1 to 20
# for i in range(1,21):
#     if(i % 2 != 0):
#         print(i)

# #Table of 57
# for i in range(1,11):
#     print(57, "x", i, "=", 57 * i)

#multiples of 3
# for i in range(1,51):
#     if(i == 15):
#         continue
#     if(i % 3 == 0):
#         print(i)

#  Find the first number divisible by both inputs
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
for i in range (1,1001):
    if(i % a == 0 and i % b == 0):
        print (i)
        break
