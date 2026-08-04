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
    
# PAN CARD 