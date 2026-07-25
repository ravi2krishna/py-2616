# Operators

# Arithmetic Operators 

num1 = 10
num2 = 5 

print("Sum Of Numbers: ", num1 + num2)
print("Difference Of Numbers: ", num1 - num2)
print("Product Of Numbers: ", num1 * num2)
print("Division Of Numbers: ", num1 / num2)
print("Modulus Of Numbers: ", num1 % num2)

print("Normal Division Of Numbers: ", 3/2) # 1.5 
print("Floor Division Of Numbers: ", 3//2) # 1

print("Exponentiation: ", 3 ** 2) # 3 ^ 2 

print("========================")

# Compound Assignment Operators

num = 10 
num = num + 5 # long form 
print(num)

num = 10 
num += 5 # short form 
print(num)

num = 10 
num *= 5 # short form 
print(num)

# Increment & Decrement increase or decrease a variable's value by one
# Increment & Decrement are used in Loops in our future sessions 

count = 0
print(count)
# count++ # SyntaxError: invalid syntax
count += 1
print(count)

count = 10
print(count)
# count-- # SyntaxError: invalid syntax
count -= 1
print(count)

print("========================")

# Comparison Operators
num1 = 3
num2 = 2

print(num1 == num2) 
print(num1 > num2)
print(num1 != num2) 

print("========================")

# Logical Operators 
num1 = 4
num2 = 3
num3 = 2
num4 = 1

print(num1 > num2) # T 
print(num3 < num4) # F 

print(num1 > num2 and num3 < num4) # T and F -> F
print(num1 > num2 and num3 > num4) # T and T -> T

print(num1 > num2 or num3 < num4) # T or F -> T

print(num1 < num2) # F
print(not num1 < num2) # T

print("========================")

# Membership Operators 
data = "python is programming language"
find_word = "java"
status = find_word in data
print(status)

data = "python is programming language"
find_word = "python"
status = find_word in data
print(status)

# List Data Type -> It's Complex Data Type To Store Multiple Values, represented using []
list_employee_ids = [101,102,103,104,105,106,108,109,110]
find_emp_id = 102
status = find_emp_id in list_employee_ids
print("Employee Found: ",status)

find_emp_id = 120
status = find_emp_id not in list_employee_ids
print("Employee Not Found: ",status)

print("========================")

# Identity Operators 
n1 = 10
n2 = 5
n3 = 10 

print(n1 is n2) 

print(id(n1))
print(id(n2))
print(id(n3))

print(n1 is n3) 

print(n1 is not n2) 

print("========================")

# Bitwise Operators 
n1 = 5 # 0000000000000101
n2 = 3 # 0000000000000011
       # 0000000000000111
       # 0000000000000001


print(n1 & n2) # 1 -> 0000000000000001
print(n1 | n2) # 7 -> 0000000000000111