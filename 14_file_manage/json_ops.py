# Working With JSON Data / Files

import json

student = {
    "id":"101",
    "name":"Ravi",
    "email":"ravi2krishna@gmail.com",
    "courses":["python","ai","cloud"],
    "gpa":9.5
}

print(type(student))
print(student)

# Write Above Data To JSON File 
with open("14_file_manage/student.json","w") as file_data:
    json.dump(student,file_data)
    
# Write Above Data To JSON File With Indentation
with open("14_file_manage/student.json","w") as file_data:
    json.dump(student,file_data,indent=4)
    
print("=" * 50)

# Read Data From JSON File
with open("14_file_manage/student.json","r") as file_data:
    data = json.load(file_data)
    print(data)
    print(type(data))
    
print("=" * 50)

# Requirement: Get Student Name & Number Of Courses he joined from student.json file
with open("14_file_manage/student.json","r") as file_data:
    data = json.load(file_data)
    
print("Student Name: ",data['name'])
print("Student Joined Courses: ",data['courses'])
print("Total Courses Enrolled By Students: ",len(data['courses']))

print("=" * 50)

# File Based - dump() and load()

# Object Based - dumps() and loads()


student = {
    "id":"101",
    "name":"Ravi",
    "email":"ravi2krishna@gmail.com",
    "courses":["python","ai","cloud"],
    "gpa":9.5
}

# dumps(): Convert a native Python dictionary into a formatted JSON string.
json_data = json.dumps(student)
print(json_data)
print(type(json_data))

print("=" * 50)

# loads(): Convert a text-based JSON string back into an Python dictionary.
string_data = '{"id": "101", "name": "Ravi", "email": "ravi2krishna@gmail.com", "courses": ["python", "ai", "cloud"], "gpa": 9.5}'
print(string_data)
print(type(string_data))

python_dict = json.loads(string_data)
print(python_dict)
print(type(python_dict))

print("=" * 50)

# Assume We Are Full Stack Developers 
# Requirement: We Have An API, When Requested We Are Getting JSON Data 
# API Which Get Users Data From Platform (ecommerce/crm/hrms)- https://dummyjson.com/users
# Find Number Of Users In Platform 

import requests 
api_url = 'https://dummyjson.com/users'
response = requests.get(api_url)
print(response) # <Response [200]>
print(response.text) # Response in str format i.e compatible with loads()
print(type(response.text)) # <class 'str'>

api_data_fetched = response.text
# Find Number Of Users In Platform
api_data_dict = json.loads(api_data_fetched)
print(type(api_data_dict)) # dict 
print(api_data_dict)

# Fetch Users Info
all_users = api_data_dict['users']
print(all_users)
print(type(all_users)) # <class 'list'>

print("=" * 50)

print("Number Of Users In Platform: ",len(all_users)) 

print("=" * 50)

# Now Give Me All The First Names Of Users In Platform 
for user in all_users:
    # print(user)
    # print("=" * 20)
    print("First Name: ", user['firstName'])

print("=" * 50)

# Now Give Me All The Young Users(age below 30) In The Platform With Their username
print("=" * 50)
print("     Young Users In The Platform")
print("=" * 50)
for user in all_users:
    if user['age'] < 30:
        print(user['username'],user['age'])
