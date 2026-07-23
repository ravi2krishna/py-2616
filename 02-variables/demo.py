# Variables

# Assign Data (Store Data)
student_name = "Ravi" 
student_age = 25
student_gpa = 9.3
student_passed = True 
student_failed = False  
STUDENT_AADHAR_ID = None # Absence of value 

# Retrieve Data (Get Data)
print(student_name)
print(student_age)
print(student_gpa)
print(student_passed)
print(student_failed)
print(STUDENT_AADHAR_ID)

# Concatenation: Joining Strings Using + Operator
print("======== Student Information ========")
# print("Student Name student_name")
# print("Student Name" student_name) # SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("Student Name: " + student_name)
# print("Student Age: " + student_age) # TypeError: can only concatenate str (not "int") to str
print("Student Age: ",student_age)
print("Student Passed: ",student_passed)
print("Student Aadhar ID: ",STUDENT_AADHAR_ID)

print('====================')

# type(): Used to tell Data Type 
type(student_name)
print(type(student_name)) # student_name is object of String Class 
print(type(student_age))
print(type(student_gpa))
print(type(student_passed))
print(type(STUDENT_AADHAR_ID))

data = {10,20,30}
print(type(data))

print('====================')

# id(): Used to tell Memory Address
id(student_name)
print(id(student_name))
print(id(student_age))
print(id(student_gpa))
print(id(student_passed))

print('====================')

# Memory Model In Python 
value_x = 10 # 4348961064
print(id(value_x))

value_y = 20 # 4348961384
print(id(value_y))

value_z = 10 # 4348961064
print(id(value_z))
