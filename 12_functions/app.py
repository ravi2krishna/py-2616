# Student Management System -> Using Functional Style 

# Menu Based System -> In Future when you learn fullstack, replace these menu with UI Elements Like Buttons 

# System Setup -> READ ONLY (Tuples)
SYSTEM_INFO = ("Digital Tech","Student Management System","v1")

# Admin Info -> READ ONLY (Tuples)
ADMIN_INFO = ("9999999999","admin@digital.com ")

# Display System Info 
print("=" * 50)
print(f"    Welcome To {SYSTEM_INFO[0]}")
print(f"    Software Is {SYSTEM_INFO[1]} - {SYSTEM_INFO[2]}")
print("=" * 50)

# Implement Core Functionalities (CRUD)
# Add Student -> ID, Name, Scores & Skills 
# Represent Data in Dictionary 
# students = {
#     "101":{
#         "name":"Ravi",
#         "scores": [80,90,80,70],
#         "skills": {"ai","python","devops"}
#         },
#     "102":{
#         "name":"john",
#         "scores": [70,90,80],
#         "skills": {"java","html","devops"}
#     }
# }

students = {}

# Add Student Function
def add_student():
# Create Student 
        print("=" * 30)
        print("     Creating Student")
        print("=" * 30)
        
        student_id = input("Enter ID: ") # 101
        
        if student_id in students:
            print("OOPS!!! Student ID Already Exists")
        else:
            name = input("Enter Name: ").title() # ravi krishna -> Ravi Krishna (transformation)
            scores = []
            while True:
                score_input = input("Enter Score or type done: ")
                if score_input == "done":
                    break 
                if score_input.isdigit():
                    score_input = int(score_input)
                    if 0 <= score_input <= 100: # 80 
                        scores.append(score_input)
                    else:
                        print("Invalid Score, Score Should Be (0-100)")
                else:
                    print("Invalid Score, Only Digits Allowed")
                    
            skills  = set()
            while True:
                skill_input = input("Enter Skill or type done: ")
                if skill_input == "done":
                    break 
                else:
                    skills.add(skill_input)
            
            print(students) # Before Adding Student
            
            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills
            }
            
            print("========== Student Added ==========")
            
            print(students) # After Adding Student 

# Update Student Function
def update_student():
# Update Student 
        print("=" * 30)
        print("     Updating Student")
        print("=" * 30)
        
        student_id = input("Enter ID To Update: ") # 101
                
        if student_id in students:
            new_name = input("Enter New Name: ").title()
            students[student_id]['name'] = new_name
            print("=" * 30)
            print("Student Updated")
            print("=" * 30)
             
        else:
            print("=" * 30)
            print("OOPS!!! Student ID Doesn't Exist")
            print("=" * 30)
        
        print(students) # After Updating Student 


# Delete Student Function
def delete_student():
# Delete Student 
        print("=" * 30)
        print("     Deleting Student")
        print("=" * 30)
        
        student_id = input("Enter ID To Delete: ") # 101
                        
        if student_id in students:
            students.pop(student_id)
            print("=" * 30)
            print("Student Deleted")
            print("=" * 30)
        else:
            print("=" * 30)
            print("OOPS!!! Student ID Doesn't Exist")
            print("=" * 30)
        
        print(students) # After Deleting Student 


# Read Student Function
def read_student():
    # Read Student 
            print("=" * 30)
            print("     Reading Student")
            print("=" * 30)
            
            student_id = input("Enter ID To Read: ") # 101
            
            if student_id in students:
                # Fetch Specific Student Data 
                data = students[student_id]
                
                # {'101': {'name': 'Ravi', 'scores': [90], 'skills': {'python'}}}
                # sid = 101
                # data = {'name': 'Ravi', 'scores': [90,80], 'skills': {'python'}}
                name = data['name'] # 'Ravi'
                scores = data['scores'] # [90,80]
                skills = data['skills'] # {'python'}
                
                # Average Score 
                average_score = sum(scores) / len(scores)
                
                # Highest Score 
                high_score = max(scores)
                        
                # Lowest Score 
                low_score = min(scores)
                
                # Skills Count
                skill_count = len(skills)
                
                # Reading Student Information
                print("=" * 30)
                print("     Reading Student Information")
                print("=" * 30)
                
                print(f"ID: {student_id}")
                print(f"Name: {name}")
                print(f"All Scores: {scores}")
                print(f"Average Score: {average_score}")
                print(f"Highest Score: {high_score}")
                print(f"Lowest Score: {low_score}")
                print(f"All Skills: {skills}")
                print(f"Skills Count: {skill_count}")
    
                
            else:
                print("=" * 30)
                print("OOPS!!! Student ID Doesn't Exist")
                print("=" * 30)    

# Search Student Function
def search_student():
    # Search Student 
            print("=" * 30)
            print("     Searching Student By Skill")
            print("=" * 30)
            
            skill_to_search = input("Enter Skill To Search: ") # python
            # premium_products = list(filter((lambda product:product['price'] > 25000),products))
            filtered_students = list(filter((lambda student_id: skill_to_search in students[student_id]['skills']),students))
            # print(filtered_students)
            
            if filtered_students:
                print("=" * 30)
                print(f"    Student With Skills {skill_to_search}")
                print("=" * 30)
            
                for student_id in filtered_students:
                    print(f"Student ID: {student_id} - Student Name {students[student_id]['name']}")
            
            else:
                print("=" * 30)
                print(f"    Student With Skills {skill_to_search} Not Found")
                print("=" * 30)

# Exit Application Function
def exit_app():
    # Exit Application
            print("=" * 30)
            print("     Exiting Application")
            print("=" * 30)
        
            # Display Admin Info 
            print("=" * 50)
            print(f"    Admin Contact Number {ADMIN_INFO[0]}")
            print(f"    Admin Email ID {ADMIN_INFO[1]}")
            print("=" * 50)
    


# Build Menu Based System For CRUD Operations 
while True:
    print("=" * 30)
    print("     Choose An Option: ")
    print("=" * 30)
    print("1 - Create Student")
    print("2 - Update Student")
    print("3 - Delete Student")
    print("4 - Read Student")
    print("5 - Search Student")
    print("6 - Exit Application")
    
    choice = input("Enter Your Choice (1-6): ")
    
    if choice == "1":
        add_student()
          
    elif choice == "2":
        update_student()

    elif choice == "3":
        delete_student()
       
    elif choice == "4":
        read_student()
        
    elif choice == "5":
        search_student()

    elif choice == "6":
        exit_app()
        break       
    else:
        # Invalid Choice 
        print("=" * 50)
        print("     Invalid Option, Only Select (1-5)")
        print("=" * 50)