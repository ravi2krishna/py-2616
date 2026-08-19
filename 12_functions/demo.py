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