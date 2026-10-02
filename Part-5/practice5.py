# Given a list of roll no .Print all unique roll nums in the list.
# rollno = {101,105,102,101,108,105,110}
# print(len(rollno))


Employees = [
(101, "Alice", 50000),
(102, "Bob", 65000),
(103, "Charlie", 45000)
]

search_id = int(input("Enter Employee ID:"))
found = False

for employee in Employees:
    employee_id = employee[0]

    if employee_id == search_id:
        print("Employee found!")
        print("Employee ID:", employee[0])
        print("Employee Name:", employee[1])
        print("Salary:",employee[2])

        found = True
        break
if found == False:
    print("Employee not found.")
