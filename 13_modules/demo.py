# Inbuilt Modules

# 1st Syntax 
# import module (imports complete module i.e loading all functionalities in module)

# print(sqrt(25)) # NameError: name 'sqrt' is not defined
# print(math.sqrt(25)) # NameError: name 'math' is not defined. Did you forget to import 'math'?

import math

print(math.pi)
print(math.sqrt(25))

print("=" * 50)

# 2nd Syntax - Recommended
# from module import specific_functionality (imports only what you need) # Recommended
from math import sqrt 
print(sqrt(25))
# print(pi) # NameError: name 'pi' is not defined

print("=" * 50)

from math import sqrt,pi,e   
print(sqrt(25))
print(pi)
print(e) 