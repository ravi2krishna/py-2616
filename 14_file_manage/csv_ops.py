# Working With CSV Files 

# Read Data 
with open("14_file_manage/students.csv","r") as file_data:
    print(file_data.read())

print("=" * 50)

# Customers Requirement: Fetch Me All Students From Hyderabad
with open("14_file_manage/students.csv","r") as file_data:
    print(file_data.read().find("Hyderabad"))
    
print("=" * 50)

# Using csv module 
import csv 
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        print(row)

print("=" * 50)

# Customers Requirement: Fetch Me All Students From Hyderabad
# Assume You Have 50k Records 
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        # print(row)
        # print(row[-1])
        if row[-1] == "Hyderabad":
            print(row)
            
print("=" * 50)

# Assume You Have 50k Records 
# Customers Requirement: Fetch Me All Students From Hyderabad and Doing Internship With tcs 
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        if row[-1] == "Hyderabad" and row[1].endswith("@tcs.com"):
            print(row)
            
print("=" * 50)

# Now Because Of Business Requirements, Companies Data Sets are Changed / Updated --> sample.csv
# Customers Requirement: Fetch Me All Students From Hyderabad
# Assume You Have 50k Records 
with open("14_file_manage/sample.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        if row[-1] == "Hyderabad":
            print(row)
            
print("=" * 50)

# Using reader 
with open("14_file_manage/sample.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        print(row)

print("=" * 50)


# Using DictReader For Dynamic Nature i.e Changing Data Sets 
with open("14_file_manage/sample.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        print(row)
# {'name': 'Hari', 'mobile': '9889032187', 'address': 'Jaipur', 'email': 'hari193@outlook.com'}
print("=" * 50)

# Now Because Of Business Requirements, Companies Data Sets are Changed / Updated --> sample.csv
# Customers Requirement: Fetch Me All Students From Hyderabad
# Assume You Have 50k Records 
with open("14_file_manage/sample.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        if row['address'] == "Hyderabad":
            print(row)
            
print("=" * 50)

# Now Because Of Business Requirements, Companies Data Sets are Changed / Updated --> sample.csv
# Customers Requirement: Fetch Me All Students From Hyderabad
# Assume You Have 50k Records 
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        if row['address'] == "Hyderabad":
            print(row)
            
print("=" * 50)

# Write Data To CSV File Using writer
with open("14_file_manage/emp.csv","w") as file_data:
    csv_writer = csv.writer(file_data)
    csv_writer.writerow(['name', 'mobile', 'address', 'email'])
    csv_writer.writerow(['Hari', '9889032187', 'Jaipur', 'hari193@outlook.com'])
    csv_writer.writerows(
        [
            ['Mahesh', '9969450859', 'Hyderabad', 'mahesh381@tcs.com'],
            ['Deepak', '9217563645', 'Ahmedabad', 'deepak3@yahoo.com']
        ]
    )
    
print("=" * 50)

# Write Data To CSV File Using DictWriter
fieldnames = ['name', 'mobile', 'address', 'email']
with open("14_file_manage/new.csv","w") as file_data:
    # csv_writer = csv.DictWriter(file_data) # TypeError: DictWriter.__init__() missing 1 required positional argument: 'fieldnames'
    csv_writer = csv.DictWriter(file_data,fieldnames)
    csv_writer.writeheader()
    csv_writer.writerow({'name': 'Mahesh', 'mobile': '9969450859', 'address': 'Hyderabad', 'email': 'mahesh381@tcs.com'})
    csv_writer.writerows(
        [
            {'name': 'Mahesh', 'email': 'mahesh381@outlook.com', 'mobile': '9969450859', 'address': 'Hyderabad'},
            {'name': 'Kishore', 'email': 'kishore349@tcs.com', 'mobile': '9900803042', 'address': 'Hyderabad'},
            {'name': 'Ravi', 'email': 'ravi96@yahoo.com', 'mobile': '9669396286', 'address': 'Hyderabad'}
        ]
    )