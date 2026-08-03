# Strings 

# Single Line Strings: Use '' or "" ""
s1 = 'hello' # Recommended
print(type(s1))
print(s1)

s2 = "hello" # Recommended
print(type(s2))
print(s2)

s3 = '''hello''' # Not Recommended
print(type(s3))
print(s3)

s4 = """hello""" # Recommended
print(type(s4))
print(s4)

# Multi Line Strings: """ """ or ''' ''''  
# define_python = "Python is a high-level, general-purpose programming language 
#         that emphasizes code readability, simplicity, and ease-of-writing 
#         with the use of significant indentation, an extensive ("batteries-included") 
#         standard library, and garbage collection."

define_python = """Python is a high-level, general-purpose programming language 
        that emphasizes code readability, simplicity, and ease-of-writing 
        with the use of significant indentation, an extensive ("batteries-included") 
        standard library, and garbage collection."""
print(type(define_python))
print(define_python)

define_python = '''Python is a high-level, general-purpose programming language 
        that emphasizes code readability, simplicity, and ease-of-writing 
        with the use of significant indentation, an extensive ("batteries-included") 
        standard library, and garbage collection.'''
print(type(define_python))
print(define_python)

# When you use single quote in a string, enclose them in double quotes 
question = "how are you ?"
# answer = 'i'm fine' # SyntaxError: unterminated string literal (detected at line 42)
answer = "i'm fine"
print(answer)

# When you use double quote in a string, enclose them in single quotes 
question = "how are you ?"
# answer = "i"m fine" # SyntaxError: unterminated string literal (detected at line 48)
answer = 'i"m fine'
print(answer)

# When you use both double quote and single quote in a string, enclose them in triple quotes 
question = "how are you ?"
# answer = 'i"m fine i'm fine' # SyntaxError: unterminated string literal (detected at line 54)
# answer = "i"m fine i'm fine" # SyntaxError: unterminated string literal (detected at line 55)
answer = '''i"m fine i'm fine'''
answer = """i"m fine i'm fine"""
print(answer)

# Accessing Strings 
text ="python"
print(text)

# Accessing Characters within string using index 
print(text[0])
print(text[1])

print(text[-1])
print(text[-2])

# print(text[10]) # IndexError: string index out of range

# print all characters one by one 
text ="python"
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])

# print all characters one by one 
text = "python is language"
print(text[0])
print(text[1])

for character in text:
    print(character)

print(dir(text)) # what actions you can do on strings

prices_products = [1000,1500,2000,2500,3000,50000]
for price in prices_products:
    print(price)

print(dir(prices_products)) # what actions you can do on lists

text = 123456789 # int 
# for character in text: # TypeError: 'int' object is not iterable
#     print(character)
    
print(dir(text)) # what actions you can do on integers, no __iter__ means no iterations 

# Slicing
text ="python"
print(text[0:4:1]) # 0123 -> pyth
print(text[0:2:1]) #  -> py
print(text[0:5:2]) #  -> pto

print(text[-4:-1:1]) #  -> tho
print(text[-4:-1:-1]) #  -> empty
print(text[-4:-6:-1]) #  -> ty