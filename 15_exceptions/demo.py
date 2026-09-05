# Exception Handling 

# When No Errors -> Nothing To Handle
print("======= Program Execution Started =======")

num1 = 10
num2 = 5

print("Result: ", num1/num2)

print("======= Program Execution Completed =======")

print("=" * 50)

# When Errors Present -> Program Stopped
# print("======= Program Execution Started =======")

# num1 = 10
# num2 = "5" # String 

# print("Result: ", num1/num2) # TypeError: unsupported operand type(s) for /: 'int' and 'str'

# print("======= Program Execution Completed =======")

# print("=" * 50)

# When Errors Present -> Let's Handle Exceptions Our Way -> Programs Don't Stop Abruptly
print("======= Program Execution Started =======")

num1 = 10
num2 = "5" # String 

try:
    print("Result: ", num1/num2) 
except:
    print("WARNING!!! Don't Divide Numbers With Strings")

print("======= Program Execution Completed =======")

print("=" * 50)

# When No Errors Present -> Let's Handle Exceptions Our Way -> Programs Don't Stop Abruptly
print("======= Program Execution Started =======")

num1 = 10
num2 = 5 

try:
    print("Result: ", num1/num2) 
except:
    print("WARNING!!! Don't Divide Numbers With Strings")

print("======= Program Execution Completed =======")

print("=" * 50)

# # Classic Exception Scenarios 
# print("======= Program Execution Started =======")

# num1 = 10
# num2 = 0 

# print("Result: ", num1/num2) # ZeroDivisionError: division by zero

# print("======= Program Execution Completed =======")

# print("=" * 50) 

# Classic Exception Scenarios 
print("======= Program Execution Started =======")

num1 = 10
num2 = 0 

try:
    print("Result: ", num1/num2) # ZeroDivisionError: division by zero
except:
    print("OOPS!!! Check more info - https://en.wikipedia.org/wiki/Division_by_zero")

print("======= Program Execution Completed =======")

print("=" * 50) 

# When Multiple Errors Come 
print("======= Program Execution Started =======")

# data = [1,2,'three',0,4]
# data = [1,2,0,4]
data = [1,2,4]

for num in data:
    print(1/num) # 1/1 - 1/2 - 1/three - 1/0 - 1/4
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    # ZeroDivisionError: division by zero
    
print("======= Program Execution Completed =======")

print("=" * 50)

# When Multiple Errors Come - Handling Exceptions
print("======= Program Execution Started =======")

data = [1,2,'three',0,4]

for num in data:
    try:
        print(1/num) # 1/1 - 1/2 - 1/three - 1/0 - 1/4
        # TypeError: unsupported operand type(s) for /: 'int' and 'str'
        # ZeroDivisionError: division by zero
    except:
        print("OOPS!!! Something Went Wrong")
    
print("======= Program Execution Completed =======")

print("=" * 50)

# When Multiple Errors Come - Handling Exceptions
print("======= Program Execution Started =======")

data = [1,2,'three',0,4]

for num in data:
    try:
        print(1/num) # 1/1 - 1/2 - 1/three - 1/0 - 1/4
        # TypeError: unsupported operand type(s) for /: 'int' and 'str'
        # ZeroDivisionError: division by zero
        # SomeOtherError: issue with program
    except TypeError:
        print("WARNING!!! Don't Divide Numbers With Strings")
    except ZeroDivisionError:
        print("OOPS!!! Check more info - https://en.wikipedia.org/wiki/Division_by_zero")
    
print("======= Program Execution Completed =======")

print("=" * 50)

# else: used to keep the code that should run, if No Exception was raised in try block
print("======= Program Execution Started =======")

num1 = 10
num2 = 5 

try:
    print("Result: ", num1/num2) # Verify Login Credentials
except:
    print("OOPS!!! Check more info - https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation Has Been Successful") # Then Only Check For OTP

print("======= Program Execution Completed =======")

print("=" * 50) 

# finally: used to keep the code that should run, whether an exception raised or not 
print("======= Program Execution Started =======")

num1 = 10
num2 = 0

try:
    print("Result: ", num1/num2) # Verify Login Credentials
except:
    print("OOPS!!! Check more info - https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation Has Been Successful") # Then Only Check For OTP
finally:
    print("Closing All Opened File Streams and Database Connections")

print("======= Program Execution Completed =======")

print("=" * 50) 