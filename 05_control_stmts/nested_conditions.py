# Nested Conditionals 
# where the inner condition is only checked if the outer condition is true. 

if True:
    print("1")
if True:
    print("This is NOT Nested Condition")

if True: # Outer Condition is True
    print("One")
    if True:
       print("This is Nested Condition") 

if False: # Outer Condition is True
    print("One")
    if True:
       print("This is Nested Condition") 

# Nested Conditional Use Case 
age = int(input('Enter Your Age: '))
if age >= 18: # usernme and password check 
    has_id = input('Do You Have ID (yes/no): ')
    if has_id == "yes": # otp check 
        print("You Can Vote")
    else:
        print("You Cannot Vote Without ID Proof")
else:
    print("You Cannot Vote - Under Age")