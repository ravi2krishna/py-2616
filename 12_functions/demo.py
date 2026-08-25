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

print("=" * 50)    
    
# Arbitrary Keyword Arguments 
def profile(**info):
    print(info)
    
# profile("ravi") # TypeError: profile() takes 0 positional arguments but 1 was given
profile(fname="Ravi")
profile(fname="ravi",lname="krishna",mobile=999999999)

print("=" * 50)   

def profile(**info):
    for data in info:
        # print(data) # key 
        print(info[data]) # value 

profile(fname="ravi",lname="krishna",mobile=999999999)

print("=" * 50)   

# Real World Use Case -> jan=3000, feb=4500, mar=9000
# Real World Use Case -> jan=3000, feb=4500, mar=9000, apr=6000
# Real World Use Case -> jan=3000, feb=4500, mar=9000, apr=6000, may=3000
# Requirement: Calculate Total Transaction Amount and Number Of Transactions Made

def bank_transactions(**transactions):
    print(transactions)
    total_transactions_value = 0
    total_transactions_count = 0
    for transaction in transactions:
        total_transactions_value += transactions[transaction]
        total_transactions_count += 1
    print(f"Total Transactions Amount is {total_transactions_value} for {total_transactions_count} Transactions")
    
bank_transactions(jan=3000, feb=4500, mar=9000)
bank_transactions(jan=3000, feb=4500, mar=9000, apr=6000, may=3000, jun=5000)

print("=" * 50)   

# return keyword 

# without return keyword 
def add(a,b):
    a + b 
    
add(10,20)
print(add(10,20))

print("=" * 50)  

# with return 
def add(a,b):
    return a + b

add(100,200)
print(add(100,200))

print("=" * 50)  

# Problem 
# def add(a,b):
#     print(a+b)

# # function composition    
# def sub(c,d,e): # add c & d then minus e --> c + d - e 
#     print(add(c,d) - e) # None - 5 
    
# sub(3,4,5) # 3 + 4 - 5 = 2  # TypeError: unsupported operand type(s) for -: 'NoneType' and 'int'


# Problem Fixed with return 
def add(a,b):
    return a+b # 7

# function composition    
def sub(c,d,e): # add c & d then minus e --> c + d - e 
    print(add(c,d) - e) # 7 - 5 
    
sub(3,4,5)    

print("=" * 50) 

# If you use return, make sure it's the last part of statement to be executed    
def add(a,b):
    print("Calculation Started")
    return a + b 
    print("Calculation Completed") # Code is structurally unreachable

print(add(1,2))

print("=" * 50)     
    
# If you have multiple return statements, first return will be considered 
a = 50
a = 60
a = 70
print(a) # 70

print("=" * 50)  

def math_ops(num1,num2):
    return num1 + num2 
    return num1 - num2 # Code is structurally unreachable
    return num1 * num2 # Code is structurally unreachable 

print(math_ops(2,3))

print("=" * 50) 

# If multiple returns are present, and used with conditionals, you can control the flow  
def math_ops(num1,num2,operator):
    if operator == "+":
        return num1 + num2 
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2 
    else:
        return "Invalid Operator"

print(math_ops(2,3,"+"))
print(math_ops(2,3,"*"))
print(math_ops(2,3,"@"))

print("=" * 50) 

# Local Scope 
def add():
    la = 10 # local - inside the function
    lb = 20 # local - inside the function
    # accessing within the function    
    print(la)
    print(lb)
    
add()

# print(la) # NameError: name 'la' is not defined. Did you mean: 'a'?
# print(lb) # NameError: name 'lb' is not defined

print("=" * 50) 

# Parameters we pass to the functions, are also local variables 
def add(la,lb): # local - la and lb are parameters to function
    print(la)
    print(lb)

add(30,40)   

# print(la) # NameError: name 'la' is not defined. Did you mean: 'a'?

print("=" * 50) 

# Global Scope 
ga = 100 # global - outside the function

def add(la,lb):
    print(la)
    print(lb)
    print(ga) # global accessed inside the function 
    
add(50,60)
print(ga)

print("=" * 50) 

# Name Conflicts
ga = 500 # global - outside the function

def add(la,lb,ga): # ga is local here 
    print(la)
    print(lb)
    print(ga)
    print(globals()['ga']) # want to access 500 
    
add(1,2,3)

print("=" * 50) 

# global variable outside the function 
count = 0 
print(count)
count += 1 
print(count)

print("=" * 50) 

# global variable inside the function 
count = 0 
print(count)
def increment():
    global count 
    count += 1 # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
    return count 

print(increment())

print("=" * 50) 

# Without Lambda Functions i.e Standard Functions 
def add(a,b):
    return a + b 
print(add(200,300))

print("=" * 50) 

# With Lambda Functions
# lambda arguments:expression 
lambda a,b:a+b 
# print((lambda_function)(arguments)) # IILE 
print((lambda a,b:a+b)(4,5)) 

print("=" * 50) 

# Without Lambda Functions i.e Standard Functions 
def is_even_num(num):
    if num % 2 == 0:
        return True 
    else:
        return False 

print(is_even_num(11))
print(is_even_num(10))

print("=" * 50) 

# With Lambda Functions
# lambda arguments:expression 
lambda num:num % 2 == 0 
print((lambda num:num % 2 == 0 )(5))
print((lambda num:num % 2 == 0 )(7))
print((lambda num:num % 2 == 0 )(6))

print("=" * 50) 

# Without Lambda Functions i.e Standard Functions
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}")

employee_info(emp_location="Hyderabad",emp_name="Ravi",emp_email="ravi2krishna@gmail.com") # Keyword Arguments 

print("=" * 50)

# With Lambda Functions
# lambda arguments:expression 
lambda emp_name,emp_email,emp_location:f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}"
print((lambda emp_name,emp_email,emp_location:f"Hi {emp_name} your email is {emp_email} and work location is {emp_location}")(emp_location="Pune",emp_name="Mike",emp_email="mike@gmail.com"))

print("=" * 50)

# Without Higher Order Function - map()
# Write a script/program to take a list of numbers and return the square of list of numbers
# [1,2,3,4,5]       ==>     [1,4,9,16,25]

def square_list(numbers):
    squared_list = []
    for num in numbers:
        squared_list.append(num * num)
    return squared_list

print(square_list([1,2,3,4,5]))

print("=" * 50)

# With Higher Order Function - map()
# Write a script/program to take a list of numbers and return the square of list of numbers
# [1,2,3,4,5]       ==>     [1,4,9,16,25]
# map(function,Iterable) 
# lambda num:num*num
map((lambda num:num*num),[1,2,3,4,5]) 
print(map((lambda num:num*num),[1,2,3,4,5]))
print(list(map((lambda num:num*num),[1,2,3,4,5])))

print("=" * 50)

# Real World Use Case - Ecommerce Application 
products = [
    {"name": "Laptop", "price": 80000, "discount": 10},
    {"name": "Phone", "price": 50000, "discount": 5},
    {"name": "Headphones", "price": 2000, "discount": 15},
    {"name": "Charger", "price": 1500, "discount": 0},
    {"name": "Camera", "price": 30000, "discount": 20},

    {"name": "Tablet", "price": 25000, "discount": 10},
    {"name": "Monitor", "price": 12000, "discount": 8},
    {"name": "Keyboard", "price": 2000, "discount": 5},
    {"name": "Mouse", "price": 1000, "discount": 0},
    {"name": "Printer", "price": 15000, "discount": 12},

    {"name": "Smartwatch", "price": 7000, "discount": 18},
    {"name": "Speaker", "price": 3500, "discount": 10},
    {"name": "PowerBank", "price": 1800, "discount": 7},
    {"name": "Router", "price": 2500, "discount": 5},
    {"name": "HardDisk", "price": 6000, "discount": 15},

    {"name": "SSD", "price": 5500, "discount": 20},
    {"name": "Webcam", "price": 2200, "discount": 10},
    {"name": "Microphone", "price": 3000, "discount": 12},
    {"name": "Projector", "price": 40000, "discount": 25},
    {"name": "Drone", "price": 75000, "discount": 30},

    {"name": "TV", "price": 45000, "discount": 18},
    {"name": "GamingConsole", "price": 38000, "discount": 15},
    {"name": "VRHeadset", "price": 20000, "discount": 22},
    {"name": "GraphicsCard", "price": 65000, "discount": 10},
    {"name": "Motherboard", "price": 12000, "discount": 8}
]

# Requirement: Give Prices After Applying discounts Without Higher Order Function
prices_after_discounts = []

for product in products:
    print(product)
    price = product['price']
    print(price)
    discount = product['discount']
    print(discount)
    
    prices_after_discount = price - (price * discount / 100)
    print(prices_after_discount)
    prices_after_discounts.append(prices_after_discount)
    
print("Prices After Discounts WithOut Higher Order Function: ",prices_after_discounts)

print("=" * 50)

# Requirement: Give Prices After Applying discounts With Higher Order Function
# map(function,Iterable) 
print(list(map((lambda product:product['price'] - product['price'] * product['discount'] / 100),products)))
print("=" * 50)
prices_after_discounts = list(map((lambda product:product['price'] - product['price'] * product['discount'] / 100),products))
print("Prices After Discounts With Higher Order Function: ",prices_after_discounts)

print("=" * 50)

# Without Higher Order Function - filter()
# Write a script/program to take a list of numbers and return the even list of numbers 
# [1,2,3,4,5,6,7,8,9,10]    ==>     [2,4,6,8,10]
def even_list(numbers):
    evened_list = []
    for num in numbers:
        if num % 2 == 0:
            evened_list.append(num)
    return evened_list 

print(even_list([1,2,3,4,5,6,7,8,9,10]))

print("=" * 50)

# With Higher Order Function - filter()
# Write a script/program to take a list of numbers and return the even list of numbers 
# [1,2,3,4,5,6,7,8,9,10]    ==>     [2,4,6,8,10]
# filter(function,Iterable)
filter((lambda num:num % 2 == 0),[1,2,3,4,5,6,7,8,9,10])
print(filter((lambda num:num % 2 == 0),[1,2,3,4,5,6,7,8,9,10]))
print(list(filter((lambda num:num % 2 == 0),[1,2,3,4,5,6,7,8,9,10])))

print("=" * 50)

# Real World Use Case - Ecommerce Application 
products = [
    {"name": "Laptop", "price": 80000, "discount": 10},
    {"name": "Phone", "price": 50000, "discount": 5},
    {"name": "Headphones", "price": 2000, "discount": 15},
    {"name": "Charger", "price": 1500, "discount": 0},
    {"name": "Camera", "price": 30000, "discount": 20},

    {"name": "Tablet", "price": 25000, "discount": 10},
    {"name": "Monitor", "price": 12000, "discount": 8},
    {"name": "Keyboard", "price": 2000, "discount": 5},
    {"name": "Mouse", "price": 1000, "discount": 0},
    {"name": "Printer", "price": 15000, "discount": 12},

    {"name": "Smartwatch", "price": 7000, "discount": 18},
    {"name": "Speaker", "price": 3500, "discount": 10},
    {"name": "PowerBank", "price": 1800, "discount": 7},
    {"name": "Router", "price": 2500, "discount": 5},
    {"name": "HardDisk", "price": 6000, "discount": 15},

    {"name": "SSD", "price": 5500, "discount": 20},
    {"name": "Webcam", "price": 2200, "discount": 10},
    {"name": "Microphone", "price": 3000, "discount": 12},
    {"name": "Projector", "price": 40000, "discount": 25},
    {"name": "Drone", "price": 75000, "discount": 30},

    {"name": "TV", "price": 45000, "discount": 18},
    {"name": "GamingConsole", "price": 38000, "discount": 15},
    {"name": "VRHeadset", "price": 20000, "discount": 22},
    {"name": "GraphicsCard", "price": 65000, "discount": 10},
    {"name": "Motherboard", "price": 12000, "discount": 8}
]

# Requirement: Find Me Premium Products i.e Products Above 25000 
premium_products = []

for product in products:
    # print(product)
    price = product['price']
    print(price)
    
    if price > 25000:
        print(product)
        premium_products.append(product)

print("Premium Products: ",premium_products)

print("=" * 50)

# Requirement: Find Me Premium Products i.e Products Above 25000 Using Higher Order 
print(list(filter((lambda product:product['price'] > 25000),products)))

print("=" * 50)

premium_products = list(filter((lambda product:product['price'] > 25000),products))
for product in premium_products:
    print(product['name'],product['price'])