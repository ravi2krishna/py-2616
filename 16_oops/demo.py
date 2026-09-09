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

# self - instance of current class
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

print("Student Name: ",student_object.student_name) # Not Recommended Style 
# print("Student Email: ",self.student_email) # Recommended Style

student_object.student_studies()

print("=" * 50)

# self - instance of current class
# Class - Blue Print 
class Student:
    
    # Student Has Something - Characteristics / Properties (Variables)
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Student Does Something - Behaviors / Actions (Methods)
    def student_studies(self):
        print("Student is studying Python")
        print("Student Name: ",student_object.student_name) # Not Recommended Style 
        print("Student Email: ",self.student_email) # Recommended Style
        
# To Use Class, Object is Required 
student_object = Student()

student_object.student_studies()

print("=" * 50)

# self - instance of current class
# Class - Blue Print 
# Working With Multiple Objects 
class Student:
    
    # Student Has Something - Characteristics / Properties (Variables)
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    
    # Student Does Something - Behaviors / Actions (Methods)
    def student_studies(self):
        print("Student is studying Python")
        print("Student Name: ",student_object.student_name) # Not Recommended Style 
        print("Student Email: ",self.student_email) # Recommended Style
        
# To Use Class, Object is Required 
student_ravi = Student()
student_ravi.student_studies()

student_john = Student()
student_john.student_studies()

student_mike = Student()
student_mike.student_studies()

print("=" * 50)

# self - instance of current class
# Class - Blue Print 
# Working With Multiple Objects Using Constructor
class Student:
    
    # Student Has Something - Characteristics / Properties (Variables)
    # student_name = "Ravi"
    # student_email = "ravi2krishna@gmail.com"
    
    # Constructor
    def __init__(self,student_name,student_email):
        print("Constructor Call")
        self.student_name = student_name
        self.student_email = student_email
        
    # Student Does Something - Behaviors / Actions (Methods)
    def student_studies(self):
        print("Student is studying Python")
        print("Student Name: ",self.student_name) # Recommended Style 
        print("Student Email: ",self.student_email) # Recommended Style
        
# To Use Class, Object is Required 
student_ravi = Student("Ravi","ravi2krishna@gmail.com")
student_ravi.student_studies()

student_john = Student("John","john@gmail.com")
student_john.student_studies()

student_mike = Student("Mike","mike@gmail.com")
student_mike.student_studies()

print("=" * 50)

# self - instance of current class
# Class - Blue Print 
# Working With Multiple Objects Using Constructor
# Working With Instance Variables
class Student:
    
    # Student Has Something - Characteristics / Properties (Variables)
    # student_name = "Ravi"
    # student_email = "ravi2krishna@gmail.com"
    
    # Constructor
    def __init__(self,student_name,student_email):
        print("Constructor Call")
        # Define Instance Variables self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
        
    # Student Does Something - Behaviors / Actions (Methods)
    # Below is an instance method 
    def student_studies(self):
        print("Student is studying Python")
        # Calling Instance Variables
        print("Student Name: ",self.student_name) # Recommended Style 
        print("Student Email: ",self.student_email) # Recommended Style
        
# To Use Class, Object is Required 
student_ravi = Student("Ravi","ravi2krishna@gmail.com")
student_ravi.student_studies()

student_john = Student("John","john@gmail.com")
student_john.student_studies()

student_mike = Student("Mike","mike@gmail.com")
student_mike.student_studies()

# self - instance of current class
# Class - Blue Print 
# Working With Multiple Objects Using Constructor
# Working With Instance Variables & Instance Methods
# Working With Class Variables & Class Methods
class Student:
    
    # Class Variable - Shared By All Objects 
    institute_name = "Digital Institute"
    
    # Constructor
    def __init__(self,student_name,student_email):
        print("Constructor Call")
        # Define Instance Variables self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
        
    # Student Does Something - Behaviors / Actions (Methods)
    # Below is an instance method 
    def student_studies(self):
        print("Student is studying Python")
        # Calling Class Variables
        # print("Institute Is: ",self.institute_name) # Not Recommended Style 
        print("Institute Is: ",Student.institute_name) # Recommended Style 
        # Calling Instance Variables
        print("Student Name: ",self.student_name) # Recommended Style 
        print("Student Email: ",self.student_email) # Recommended Style
        
    
    # Class Method
    @classmethod
    def change_institute_name(cls,new_institute_name):
        cls.institute_name = new_institute_name
        # print("Student Name: ",self.student_name) # Accessing Instance Variables inside class methods gives Error 
        
        
# To Use Class, Object is Required 
student_ravi = Student("Ravi","ravi2krishna@gmail.com")
student_ravi.student_studies()

student_john = Student("John","john@gmail.com")
student_john.student_studies()

student_mike = Student("Mike","mike@gmail.com")
student_mike.student_studies()

# Calling Class Method To Change Institute Name
Student.change_institute_name("New Digital Institute")

student_ravi = Student("Ravi","ravi2krishna@gmail.com")
student_ravi.student_studies()

student_john = Student("John","john@gmail.com")
student_john.student_studies()

student_mike = Student("Mike","mike@gmail.com")
student_mike.student_studies()
