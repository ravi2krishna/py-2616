# Dictionaries

# empty dict 
empty_dict = {}
print(empty_dict)
print(type(empty_dict))

empty_dict = dict() # dict is immutable sequence
print(empty_dict)
print(type(empty_dict))

# dict with Numeric Data 
data = {1:10,2:20,3:30,4:40,5:50}
print(data)

# dict with Text Data 
data = {"c1":"python","c2":"ai","c3":"cloud"}
print(data)

# dict with Mixed Data 
data = {1:10,2:20,3:30,"c1":"python","c2":"ai","gpa":7.8,"passed":True}
print(data)

# Accessing Data In tuples
data = {1:10,2:20,3:30,4:40,5:50}
print(data)

# first element 
# first_element = data[0] # KeyError: 0
first_element = data[1]
print(first_element)

# last element 
last_element = data[5]
print(last_element)

# unknown element 
# unknown_element = data[10] # KeyError: 10
# print(unknown_element)

# Access Individual Elements
data = {1:10,2:20,3:30,4:40,5:50}
print(data[1]) # data[key]
print(data[2])
print(data[3])
print(data[4])
print(data[5])

print("=" * 20)

# Access Individual Elements -> 50k elements 
data = {1:10,2:20,3:30,4:40,5:50,1000:10000}
# print(dir(data)) # __iter__
for num in data: # only keys we got 
    print(num) 

print("=" * 20)

for key in data: # only keys we got 
    print(key) 

print("=" * 20)

for key in data: # only keys we got 
    print(data[key]) # get values using keys 

print("=" * 20)

# Apply Operators -> Requirements: Multiply Each Number with 10
data = {1:10,2:20,3:30,4:40,5:50}
for key in data:
    print(data[key] * 10)
    
print("=" * 20)

# Apply Conditions -> Requirements: Give Only Even Numbers
data = {1:10,2:20,3:35,4:40,5:55}
for key in data:
    if data[key] % 2 == 0:
        print(data[key])
    
print("=" * 20)

# Duplicates Allowed - Values 
data = {1:10,2:20,3:30,4:10,5:50}
print(data)

print("=" * 20)

# Duplicates Keys Will Override the data 
data = {1:10,2:20,1:30,4:10,5:50}
print(data)

# Values Can Be Any Kind Of Objects  
data = {1:10,2:20,3:30,"c1":"python","c2":"ai","gpa":7.8,"passed":True}
print(data)

# Key Can Be Only Immutable Objects 
data = {'ten':10,'twenty':20}
print(data)

# data = {['ten']:10,['twenty']:20} # TypeError: unhashable type: 'list'
# print(data)

data = {('ten'):10,('twenty'):20} 
print(data)

# Insertion Order Is Preserved 
data = {1:10,2:20,2:30,4:40,5:50}
print(data)

# Mutable / Immutable -> Dictionaries are Mutable 
data[1] = 100
print(data)

# Real World Dictionaries Looks like JSON Data 
# https://media.licdn.com/dms/image/v2/D4D12AQGwOUMYbhUu-A/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1682148646113?e=2147483647&v=beta&t=qeCSY5Ktzx2jkeq7suYaSBV_-OS_18P-yuabrIhNWcU
# https://www.anbowell.com/_astro/guide_to_json.DimYsN86.webp
# https://www.goanywhere.com/sites/default/files/styles/max_2600x2600/public/2022-08/example_json_file_0.png.webp?itok=nS3qt8dd

students = {"101":{},"102":{}}
print(type(students))

students = {
    "101":{
        "name":"Ravi",
        "email": "ravi2krishna@gmail.com",
        "courses": ["python","ai","cloud"],
        "courses_fee": (10000,25000,15000) 
        },
    "102":{
        "name":"john",
        "email": "john@gmail.com",
        "courses": ["java","ai","devops"],
        "courses_fee": (10000,25000,15000) 
    }
    }
print(type(students))

print(students)

print("=" * 50)

# Requirement: get 101 student details
print(students["101"])

print("=" * 50)

# Requirement: get 101 student enrolled courses
print(students["101"]["courses"])

print("=" * 50)

# Requirement: get 101 student second course
print(students["101"]["courses"][1])

# dict Operations / Methods 
print(dir(data))