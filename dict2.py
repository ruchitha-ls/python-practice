'''Create a dictionary with n employee details. The key - value 
pair represents an employee information such as employee grade and 
salary. Calculate the average salary of all the employees whose 
grade is A and B.
Note: The user can give grade either in upper or lower case''' 

n= int(input("Enter the number of employees: "))
print("Enter employee details(Employee Grade and Salary)")
d1= {}
for i in range(n):
    print(f"\nEntering details for employee {i+1}")
    grade = input("Enter Employee Grade: ")
    salary = int(input("Enter Employee Salary: "))
    d1[grade]= salary

avg=0
for grade in d1:
    if grade in 'a, b, A, B':
        avg=d1[grade]+avg
    else:
        continue
print(f"\nThe average salary of all employees with A or B grade is: {avg}")
