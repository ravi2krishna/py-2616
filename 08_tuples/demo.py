# Tuples 

# empty tuple 
empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))

empty_tuple = tuple() # tuple is immutable sequence
print(empty_tuple)
print(type(empty_tuple))

# tuple with Numeric Data 
data = (10,20,30,40,50)
print(data)

# tuple with Text Data 
data = ("python","ai","cloud")
print(data)

# tuple with Mixed Data 
data = (10,20,30,"python","ai",7.8,True)
print(data)

# Accessing Data In tuples
data = (10,20,30,40,50)
print(data)

# first element 
first_element = data[0]
print(first_element)

# last element 
last_element = data[-1]
print(last_element)

# unknown element 
# unknown_element = data[10] # IndexError: tuple index out of range
# print(unknown_element)

# Slicing In tuples same as strings 
data = (10,20,30,40,50)
print(data)
print(data[1:3:1])# 20, 30
print(data[0:5:2])# 10,30,50

# Access Individual Elements
data = (10,20,30,40,50)
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])

print("=" * 20)

# Access Individual Elements -> 50k elements 
data = (10,20,30,40,50000)
# print(dir(data)) # __iter__
for num in data:
    print(num)

print("=" * 20)

# Apply Operators -> Requirements: Multiply Each Number with 10
data = (10,20,30,40,50)
for num in data:
    print(num * 10)
    
print("=" * 20)


# Apply Conditions -> Requirements: Give Only Even Numbers
data = (10,20,35,40,55)
for num in data:
    if num % 2 == 0:
        print(num)
    
print("=" * 20)

# Duplicates Allowed 
data = (10,20,10,30,40,10,50)
print(data)

print("=" * 20)

# Insertion Order Is Preserved 
data = (10,20,10,30,40,10,50)
print(data)

# tuple Operations / Methods 
print(dir(data))