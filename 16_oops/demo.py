# OOP - Object Oriented Programming 

# Class - Blue Print 
class Student:
    
    # Student Has Something - Characteristics / Properties (Variables)
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Student Does Something - Behaviors / Actions (Methods)
    def student_studies():
        print("Student is studying Python")
        
# To Use Class, Object is Required 
student_object = Student()

# print("Student Name: ",student_name) # NameError: name 'student_name' is not defined
# print("Student Email: ",student_email) # NameError: name 'student_email' is not defined

print("Student Name: ",student_object.student_name)
print("Student Email: ",student_object.student_email)

# student_object.student_studies() # TypeError: Student.student_studies() takes 0 positional arguments but 1 was given

print("=" * 50)

# It's a function, as it's outside the class 
# def student_studies():
#     print("Student is studying Python")
    
# Class - Blue Print 
class Student:
    
    # Student Has Something - Characteristics / Properties (Variables)
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Student Does Something - Behaviors / Actions (Methods)
    def student_studies(self):
        print("Student is studying Python")
        
# To Use Class, Object is Required 
student_object = Student()

# print("Student Name: ",student_name) # NameError: name 'student_name' is not defined
# print("Student Email: ",student_email) # NameError: name 'student_email' is not defined

print("Student Name: ",student_object.student_name)
print("Student Email: ",student_object.student_email)

student_object.student_studies()