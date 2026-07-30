# Looping Structures (Iteration Statements) - Repetition

# "while" loop 

# while True: # Always True -> This Forms Infinite Loop
#     print("Repeat....")
#     print("Code............")

# To terminate above use control + c 

while False: # Code is not analyzed because condition is statically evaluated as false
    print("Repeat....")
    print("Code............")
    
# Counters 
count = 1
while count <= 5: # 6 <= 5 (False)
    print(f"Count Is {count}")
    count += 1
    
# use while loop, when we don't know number of Iterations/Repetitions in advance

# You Found a Lost Phone, Trying To Break Password / PIN 
# Tell me at which attempt, the Phone will be unlocked ?? 

actual_pin = "2345"
user_given_pin = ""

while actual_pin != user_given_pin:
    user_given_pin = input("Enter PIN To Unlock: ")
print("Phone Unlocked")
    

# for loop 
prices_products = [1000,1500,2000,2500,3000,50000]

# Requirement: Some Offer is running -> Provide a discount of 250 on each product 
# In Lists We Have Index, Which Starts From Zero and keeps incrementing 
# list[index]
print("Prices Before Discount")
print(prices_products[0])
print(prices_products[1])

print("Prices After Discount")
print(prices_products[0] - 250)
print(prices_products[1] - 250)
# .
# .
# .
# print(prices_products[14999] - 250)

print("Prices Before Discount")
prices_products = [1000,1500,2000,2500,3000,3500,4000,4500,5000,50000]
for price in prices_products:
    print(price)
    
print("Prices After Discount")
for price in prices_products:
    print(price - 250)
    
