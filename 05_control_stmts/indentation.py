# Indentation Rules 

# -> When to use Space -> When We Write Block Of Code
# -> When Not to use Space -> Single Statement 
# -> How many spaces to use -> At least one space, but recommended is 4 Spaces (tab)

print("Good Morning")
# print("Good Morning") # IndentationError: unexpected indent

# class Student: # IndentationError: expected an indented block after class definition on line 10
# student_id = 101
# student_name = "Ravi"
# student_email = "ravi2krishna@gmail.com"

class Student: 
  student_id = 101
  student_name = "Ravi"
  student_email = "ravi2krishna@gmail.com"
 
# recommended is 4 Spaces (tab)
class Car: 
    car_brand = "Tata"
    car_model = "Punch"
    
class Person: 
                            person_name = "Human"