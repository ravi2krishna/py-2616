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
