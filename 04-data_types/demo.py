# Data Types 

# Numeric Types 

data = 10
print(type(data))

data = 10.5
print(type(data))

# complex: In Maths We Have a + ib 
# data = 3 + i5 # NameError: name 'i5' is not defined. Did you mean: 'id'?
# print(type(data))

# complex: In Python We Have a + bj 
data = 3 + 5j
print(type(data))

# Boolean Type
data = True 
print(type(data))

data = False 
print(type(data))

# None Type
data = None 
print(type(data))

# String Type 
data = "Python"
print(type(data))

# Complex Data Types 

# List 
data = [1,2,3,4,5]
print(type(data))

# Tuple 
data = (1,2,3,4,5)
print(type(data))

# Set 
data = {1,2,3,4,5}
print(type(data))

# Dictionary 
data = {"course":"python","duration":30}
print(type(data))

# Custom Data Type For Students 
class Student:
    student_id = 101
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    student_enrolled_courses = ["Python","DevOps","Cloud"]
    student_enrolled_courses_prices = (10000,25000,15000)
    
data = Student() # OOP -> Object Creation 
print(type(data))

# Type Conversion / Implicit Conversion [Automatic] 
n1 = 10 # int 
n2 = 5.5 # float 
sum = n1 + n2 # float 
print(sum)
print(type(sum))

# Type Casting / Explicit Conversion [Manual]
price = 1150.12 
print(price)
print(type(price))

# Round off price 
price = int(price) # Type Casting
print(price)
print(type(price))

# Some User in a web site was filling some form (text boxes) 
# Behind the scenes these are strings

rating = "1"
print(type(rating))

# if rating >= 4: # TypeError: '>=' not supported between instances of 'str' and 'int'
rating = int(rating)
if rating >= 4:
    print("Positive Feedback") 
else:
    print("Negative Feedback") 


