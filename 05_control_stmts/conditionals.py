# Conditional Structures

# if 

if True:
    print("This")
    print("Is")
    print("Block")
    print("Of")
    print("Code")

print("=================")
    
if False: # Code is not analyzed because condition is statically evaluated as false
    print("This")
    print("Is")
    print("Block")
    print("Of")
    print("Code")
    
if 5 > 2: # True
    print("Yes 5 > 2 Is Correct")
    
if 5 < 2: # False
    print("Yes 5 < 2 Is Correct")
    
num = 10 
if num > 0:
    print("Given Num Is Positive")
if num < 0:
    print("Given Num Is Negative")
 
print("=================")

# if else  
   
num = -10 
if num > 0:
    print("Given Num Is Positive")
else:
    print("Given Num Is Negative")

print("=================")    

name = "Ravi"
print(name)

# input() function - Reads Input 
name = input("Enter Your Name: ")
print(name)
print("Welcome: "+name) # Concatenation 
print("Welcome: ",name) # Comma Operator 
print("Welcome: {name}") # No Interpolation
print(f"Welcome: {name}") # Interpolation

print("=================")
  
num = int(input("Enter Number: "))
if num > 0: # TypeError: '>' not supported between instances of 'str' and 'int'
    print("Given Num Is Positive")
else:
    print("Given Num Is Negative")
    
print("=================")
  
num = int(input("Enter Number: "))
if num > 0: 
    print(f"Given Num {num} Is Positive")
else:
    print(f"Given Num {num} Is Negative")

print("=================")

# Voting App 
age = int(input("Enter Your Age: "))
if age >= 18:
    print("You Can Vote")
else:
    print("You Cannot Vote")

print("=================")

# Conditional Expression 
# value_if_true if condition else value_if_false
print("You Can Vote" if age >= 18 else "You Cannot Vote")
# print(status)