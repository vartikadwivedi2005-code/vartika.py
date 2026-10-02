# Complex Datatypes - List , Tuple , Set , Dictionary
# List  - mutable

# marks = [67,90,87,98]
# print(marks,type(marks))

# length
# print(len(marks))

# index
# print(marks[1])
# print(marks[-1])

# slicing a list - list(start:end)
# print(marks[0:3])
# print(marks[-3:-1])
# print(marks[:])

# loop
# for score in marks:
#     print(score)

# append
# marks.append(50)
# print(marks)

# # insert
# marks.insert(0,50)
# print(marks)

# print(97 in marks)
# marks.clear()
# print(marks)
# print(marks,len(marks))



# Tuple - immutable
# marks = (34,78,55,78,90)
# print(marks[2])

# # count the occurance of a number
# print(marks.count(55))

# # index
# print(marks.index(90))

# print(type(marks))



# # Set => unique items collection

# # marks = {90,98,97,96,96}
# # print(len(marks))
# # # duplicates not stored

# # for score in marks:
# #     print(score)



# # Dictionary word => meaning   {key => val}    - mutable

marks ={"Math":99 ,"Physics":98 , "Chemistry":97}
# print(marks,type(marks))

# print(marks["Physics"])

# marks["Physics"] = 99
# print(marks["Physics"])

# marks["English"] = 95
# print(marks["English"])

for key in marks:
    print(key,marks[key])






