# Check num is odd or even
# def check_odd_even(number):
#     if number % 2 == 0:
#         print(number,"is even")
#     else:
#         print(number,"is odd")

# check_odd_even(12)
# check_odd_even(7)


# count vowels
# def count_vowels(text):
#     count = 0

#     for character in text.lower():
#         if character in "aeiou":
#             count += 1
#     return count

# result = count_vowels("Tony Stark")
# print("Number of vowels:", result)


# check whether no is prime or not
# def check_prime(number):
#     if number<=1:
#         print(number,"is not prime")
#         return
#     for i in range(2,number):
#         if number % i == 0:
#             print(number, "is not prime")
#             return
#     print(number, "is prime")
# check_prime(7)
# check_prime(10)


# return average marks
def calculate_average(marks):
    if len(marks) == 0:
       return 0
    average = sum(marks)  / len(marks)
    return average
student_marks = [85, 90, 78, 92, 80]
result = calculate_average(student_marks)
print("Average marks:", result)