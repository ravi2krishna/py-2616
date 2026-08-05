# String Methods 
greet = "hi"
print(type(greet))
print(greet)

# Requirement is print Hi
# capitalize(): Return a copy of the string with its first character capitalized and the rest lowercased.
result = greet.capitalize()
print(result)
print(greet)

# String methods allows for various manipulations, transformations, and checks(validations).

# Simulate Gmail Functionality - Transformation
#                        RaVI2KRisHnA -> ravi2krishna@gmail.com 

email = input("Enter Email ID: ")
print("Original Email Given: "+email)

# lower(): method returns a string where all characters are lower case.
transformed_email = email.lower()
print("Transformed Email: "+transformed_email)

# strip(): to remove spaces from both left and right sides
# lstrip(): to remove spaces from the left side only.
# rstrip(): to remove spaces from the right side only.

transformed_email = transformed_email.strip()
print("Transformed Email: "+transformed_email)

# add domain @gmail.com using concatenation 
domain = "@gmail.com"
transformed_email = transformed_email + domain
print("Transformed Email: "+transformed_email)

# Simulate Phone ISD Scenario 
# https://us1.discourse-cdn.com/flex016/uploads/weweb/original/2X/d/dbe25afb4aeb05640347e2f7c1b7ae532ebb28f2.png
# https://www.businessbloomer.com/wp-content/uploads/2014/11/woocommerce-add-coupon-automatically-to-cart-if-product.png

contact_number = input("Enter Contact Number Starting With ISD CODE: ")
# contact_number = contact_number.startswith("+91")
# print(f"Indian Number ? {contact_number}")

# startswith(): returns True if a string starts with a specified prefix; otherwise, it returns False
if contact_number.startswith("+91"):
    print("Calling India - Charged In Rupees")
elif contact_number.startswith("+33"):
    print("Calling France - Charged In Euros")
elif contact_number.startswith("+1"):
    print("Calling USA - Charged In Dollars")
else:
    print("Invalid Number")
    
# Simulate PAN CARD Functionality - Validations (Checks)
# https://www.pan.utiitsl.com/
# https://www.pan.utiitsl.com//PANform/forms/csf/preCSF - Build This
pan = input("Enter PAN ID: ")
print("Original PAN: "+pan) # @akll9912w

# isalnum(): method returns True if the string contains only letters and numbers, otherwise False
valid_pan = pan.isalnum() and len(pan) == 10
print(f"Given PAN {pan} is {valid_pan}") 
length_pan = len(pan)
print("Length Of Pan: ",length_pan)

# https://www.pancardapp.com/assets/img/form-pages/duplicate-pan-card/duplicate-pan-card.jpg
# ABCDE1234A
if len(pan) == 10:
    first_five = pan[0:5:1] # ABCDE
    middle_four = pan[5:9:1] # 1234 
    last_one = pan[9] # A 
    
    # isalpha() method returns True if all characters in a string are alphabetic letters
    # isdigit() method returns True if all characters in the string are digits
    if first_five.isalpha() and middle_four.isdigit() and last_one.isalpha():
        # upper() method returns Upper cased string 
        print("Transforming Pan: "+pan.upper())
    else:
        print(f"Given Pan {pan} is Invalid")
        
else:
    print("Pan Should be 10 Characters Exactly")
    
    
# Simulate Data Operations Work: CSV Data from a file and perform some operations 
# https://www.datablist.com/learn_images/csv/google_sheet_csv.png
# https://www.slashgear.com/img/gallery/csv-files-explained-what-they-are-and-how-to-open-them/what-are-csv-files-1699455969.jpg
# Name,Email,Age,City,Job_Role
# emp_data = "John,john@apple.com,30,Hyderabad,Developer"
# Requirement: Display Employee Name & Job Role

emp_data = "John,john@apple.com,30,Hyderabad,Developer"
emp_name = emp_data[0:4]
print("Employee Name: ",emp_name)

# Records Updated in future, employee transferred 
emp_data = "Michael,michael@apple.com,30,Hyderabad,Developer"
emp_name = emp_data[0:4]
print("Employee Name: ",emp_name)

# split() method breaks a string into a list of substrings based on a specified delimiter, default being space
emp_data = "Michael,michael@apple.com,30,Hyderabad,Developer"
data_splitted = emp_data.split()
print(data_splitted)


emp_data = "Michael,michael@apple.com,30,Hyderabad,Developer"
emp_data = "michelangelo,michelangelo@apple.com,30,Hyderabad,Developer"
data_splitted = emp_data.split(",")
print(data_splitted)

print("Employee Name: ", data_splitted[0])
print("Employee Job Role: ", data_splitted[-1])