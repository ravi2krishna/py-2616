# Sets 

# empty dict 
empty_set = {} # This is Dictionary, Empty Sets Cannot be created with symbols {}
print(empty_set)
print(type(empty_set))

empty_set = set() # Unordered & Unique Elements
print(empty_set)
print(type(empty_set))

# sets with Numeric Data 
data = {10,20,30,40,50}
print(type(data))
print(data)

data = [10,20,30,40,50]
print(type(data))
print(data)

# set with Text Data 
data = {"python","ai","cloud"}
print(data)

# tuple with Mixed Data 
data = {10,20,30,"python","ai",7.8,True}
print(data)

# # Accessing Data In sets 
data = {10,20,30,40,50}

# # first element 
# first_element = data[0] # TypeError: 'set' object is not subscriptable
# print(first_element)

# # last element 
# last_element = data[-1]
# print(last_element)


print("=" * 20)

# Access Individual Elements -> 50k elements 
data = {10,20,30,40,50000}
# print(dir(data)) # __iter__
for num in data:
    print(num)

print("=" * 20)

# Apply Operators -> Requirements: Multiply Each Number with 10
data = {10,20,30,40,50}
for num in data:
    print(num * 10)
    
print("=" * 20)

# Apply Conditions -> Requirements: Give Only Even Numbers
data = {10,20,35,40,55}
for num in data:
    if num % 2 == 0:
        print(num)
    
print("=" * 20)

# Duplicates Allowed & Insertion Order Not Preserved 
data = {10,20,10,30,40,10,50}
print(data)

print("=" * 20)

# tuple Operations / Methods 
print(dir(data))

# frozenset 
data = frozenset({10,20,30,40,50})
print(data)
print(type(data))
print(dir(data))