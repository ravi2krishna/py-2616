# Functional Programming 

# Without Functions 

# User One Wants To Calculate For Below Values 
num1 = 10
num2 = 5 

# Math Operations
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 50)

# User Two Wants To Calculate For Below Values 
num1 = 20
num2 = 5 

# Math Operations
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 50)

# User Three Wants To Calculate For Below Values 
num1 = 30
num2 = 5 

# Math Operations
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

print("=" * 50)

# With Functions 
def math_ops():
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)

# User One Wants To Calculate For Below Values 
num1 = 10
num2 = 5 
math_ops()
print("=" * 50)
# User Two Wants To Calculate For Below Values 
num1 = 20
num2 = 5 
math_ops()
print("=" * 50)
# User Three Wants To Calculate For Below Values 
num1 = 30
num2 = 5 
math_ops()
print("=" * 50)

# math_ops(10,5) # TypeError: math_ops() takes 0 positional arguments but 2 were given

# With Functions & Parameters
def math_ops(num1,num2): # num1,num2 are Parameters
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)
    
# math_ops() # TypeError: math_ops() missing 2 required positional arguments: 'num1' and 'num2'
math_ops(10,5) # User One
math_ops(20,5) # User Two
math_ops(30,5) # User Three

print("=" * 50)

# Process Data 
def process_string(email_id):
    print(email_id.lower()+"@gmail.com")

process_string("RAvi2KRiShNA")
process_string("JOHn_kYLE")

print("=" * 50)

# Positional Arguments 
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}")

# employee_info("Hyderabad","Ravi")  # TypeError: employee_info() missing 1 required positional argument: 'emp_location'  
employee_info("Hyderabad","Ravi","ravi2krishna@gmail.com")
print("=" * 50)
employee_info("Ravi","ravi2krishna@gmail.com","Hyderabad")
print("=" * 50)

# Keyword Arguments 
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}")

employee_info("Hyderabad","Ravi","ravi2krishna@gmail.com")
print("=" * 50)
employee_info(emp_location="Hyderabad",emp_name="Ravi",emp_email="ravi2krishna@gmail.com") # Keyword Arguments 
print("=" * 50)

# Without Default Arguments 
def employee_info(emp_name,emp_email,emp_location,org_name):
    print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} at location {emp_location}")
    
employee_info(emp_location="Hyderabad",emp_name="Ravi",emp_email="ravi2krishna@gmail.com",org_name="IBM") 
employee_info(emp_location="Bangalore",emp_name="Ram",emp_email="ram@gmail.com",org_name="IBM") 
employee_info(emp_location="Pune",emp_name="John",emp_email="john@gmail.com",org_name="IBM") 
employee_info(emp_location="Chennai",emp_name="Khan",emp_email="khan@gmail.com",org_name="IBM") 

print("=" * 50)

# With Default Arguments 
def employee_info(emp_name,emp_email,emp_location,org_name="IBM"):
    print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} at location {emp_location}")
    
employee_info(emp_location="Hyderabad",emp_name="Ravi",emp_email="ravi2krishna@gmail.com") 
employee_info(emp_location="Bangalore",emp_name="Ram",emp_email="ram@gmail.com") 
employee_info(emp_location="Pune",emp_name="John",emp_email="john@gmail.com") 
employee_info(emp_location="Chennai",emp_name="Khan",emp_email="khan@gmail.com") 
employee_info(emp_location="New York",emp_name="Mike",emp_email="mike@gmail.com",org_name="META") 
print("=" * 50)

# Placement Requirement: Default arguments
# def employee_info(emp_name,emp_email,emp_location,org_name="IBM",emp_mobile):
#     print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} at location {emp_location}")

# Non-default argument follows default argument
# SyntaxError: parameter without a default follows parameter with a default

def employee_info(emp_name,emp_email,emp_location,emp_mobile,org_name="IBM",org_gst="27ABCDE1234F1Z5"):
    print(f"Hi {emp_name} your email is {emp_email} and working for {org_name} at location {emp_location}")

print("=" * 50)

# Without Arbitrary Positional Arguments 
def add_numbers(n1):
    print(n1)

def add_numbers_two(n1,n2):
    print(n1+n2)
    
def add_numbers_five(n1,n2,n3,n4,n5):
    print(n1+n2+n3+n4+n5)    
    
def add_numbers_ten(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10):
    print(n1+n2+n3+n4+n5+n6+n7+n8+n9+n10)    
    
add_numbers(10)    
add_numbers_two(1,2)   
add_numbers_five(1,2,3,4,5)
add_numbers_ten(1,2,3,4,5,6,7,8,9,10)

print("=" * 50)

# With Arbitrary Positional Arguments 
def add_numbers(*numbers):
    print(numbers)
    
add_numbers(10)    
add_numbers(1,2)   
add_numbers(1,2,3,4,5)
add_numbers(1,2,3,4,5,6,7,8,9,10)

print("=" * 50)

# Now Add Numbers and give sum  
def add_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num 
    print(f"Total Sum is {total}")
    
add_numbers(10)    
add_numbers(1,2)   
add_numbers(1,2,3,4,5)
add_numbers(1,2,3,4,5,6,7,8,9,10)

print("=" * 50)

def profile(*info):
    print(info)

profile("ravi")
profile("ravi","krishna")
profile("ravi","krishna",999999999)
profile("ravi","krishna",999999999,False,9.5)

print("=" * 50)

# Real World Use Case w.r.t Ecommerce Cart Functionality 
def cart_value_value(*products):
    total_cart = 0
    for num in products:
        total_cart += num 
    print(f"Total Cart Value is {total_cart}")    

cart_value_value(1999.00,299.00,3049.00)
    