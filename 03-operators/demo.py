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