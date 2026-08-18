# Student Management System

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

# Build Menu Based System For CRUD Operations 
while True:
    print("=" * 30)
    print("     Choose An Option: ")
    print("=" * 30)
    print("1 - Create Student")
    print("2 - Update Student")
    print("3 - Delete Student")
    print("4 - Read Student")
    print("5 - Exit Application")
    
    choice = input("Enter Your Choice (1-5): ")
    
    if choice == "1":
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
        
    elif choice == "2":
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

    elif choice == "3":
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
       

    elif choice == "4":
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
            total_score = 0 # 0 + 90 + 80
            count_scores = 0 # 0 + 1 + 1 
            
            for score in scores: # 90, 80 
                total_score += score
                count_scores += 1 
            
            average_score = total_score / count_scores
            
            # Highest Score 
            high_score = scores[0] # 100
            
            for score in scores: # 90, 80, 100 
                if score > high_score:
                    high_score = score
                    
            # Lowest Score 
            low_score = scores[0] # 100
            
            for score in scores: # 90, 80, 100 
                if score < low_score:
                    low_score = score
            
            # Skills Count
            skill_count = 0
            for skill in skills:
                skill_count += 1
            
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

    elif choice == "5":
        # Exit Application 
        print("=" * 30)
        print("     Exiting Application")
        print("=" * 30)
    
        # Display Admin Info 
        print("=" * 50)
        print(f"    Admin Contact Number {ADMIN_INFO[0]}")
        print(f"    Admin Email ID {ADMIN_INFO[1]}")
        print("=" * 50)
        break
        
    else:
        # Invalid Choice 
        print("=" * 50)
        print("     Invalid Option, Only Select (1-5)")
        print("=" * 50)