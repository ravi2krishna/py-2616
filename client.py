# Client Needs Math Package 

# from package_name.module_name import function_name 

from mathpackage.add import msg,add_fun

print(msg)
print("Sum Of Numbers: ",add_fun(10,20))

print("=" * 50)

from mathpackage import add 
print(add.msg)
print(add.add_fun(20,30))

print("=" * 50)
