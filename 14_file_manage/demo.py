# File Management With Python 

# Syntax - 1 

# file = open("file_path","mode") 
# file = open("file.txt","r") 

# file_data = open("file.txt","r") # FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'
# print(file_data)

file_data = open("14_file_manage/file.txt","r") 
print(file_data)

print(file_data.closed) # False --> Still Open 
file_data.close() # Flush and close the IO object.
print(file_data.closed) # True --> Now File Closed

print("=" * 50)

# Syntax - 2 (Recommended)
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data) 
print(file_data.closed) # True --> File Implicitly Closed

print("=" * 50)

# Read Data From File Using Python - r mode
with open("14_file_manage/file.txt","r") as file_data:
    print(file_data.read())

print("=" * 50)
 
# Create File Using Python - w mode 
with open("14_file_manage/write.txt","w") as file_data:
    print("File Created")
    
print("=" * 50)

# Update File Using Python - w mode 
with open("14_file_manage/write.txt","w") as file_data:
    file_data.write("This is data updated with python")
    
print("=" * 50)

# Delete File Using Python - You must import the os module and provide the file path
# file_path = "14_file_manage/new.txt"
file_path = "14_file_manage/write.txt"
import os 
os.remove(file_path)    

print("=" * 50)

# Directory Management - os module 
directory_path = "14_file_manage/students_data"
# Create Directory
if not os.path.exists(directory_path):
    os.mkdir(directory_path)
# Delete Directory
os.rmdir(directory_path)
