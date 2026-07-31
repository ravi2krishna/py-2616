# Branching Structures (Jump Statements) 

for num in range(1,11,1):
    print(num)
    
print("==============")

# break: helps you exit loops 
for num in range(1,11,1):
    # stop the loop, when num is 5
    if num == 5: # 20k employees, find emp_id, found at 12500 stop here
        break
    print(num)

print("==============")

# continue: helps you skip the current iteration 
for num in range(1,11,1):
    # skip the current iteration, when num is 5
    if num == 5: # 20k employees, skip bonus for emp_id found at 12500 skip for this employee
        continue
    print(num)
    
print("==============")

# pass: acts as a placeholder, to do nothing 
# Requirement - To Perform Some Operations in the Future 
# When Salary is above 25000, we want to do something in the Future 

emp_salary = 15000
if emp_salary > 25000:
    # we want to do something in the Future 
    pass # __________________

# Other Operations To Work On 
print("Working With Next Functionalities")

# After 6 Months in the Future 
# When Salary is above 25000, we want to do something 
# something is promoted to permanent employee

emp_salary = 35000
if emp_salary > 25000:
    print("Promoted To Permanent Employee")

# When Working With OOP 
class Student:
    student_id = 101
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    student_enrolled_courses = ["Python","DevOps","Cloud"]
    student_enrolled_courses_prices = (10000,25000,15000)

# Park Employee    
class Employee:
    pass 

class Manager:
    pass 

class Developer:
    pass 