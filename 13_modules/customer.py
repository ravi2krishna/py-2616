# Now Customer Wants To Use arithmetic operations and profile related information

from mathprofile import maintainer
print("Maintainer Is: "+maintainer)
# print("Institute Is: "+institute) # NameError: name 'institute' is not defined

print("=" * 50)

from mathprofile import maintainer,institute,add 
print("Maintainer Is: "+maintainer)
print("Institute Is: "+institute)
print("Adding Numbers: ",add(10,20))


