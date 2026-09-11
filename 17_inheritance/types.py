# Types Of Inheritance 

# Single Level Inheritance: One Parent -> One Child 
class Father:
    def house(self):
        print("Has House")
        
class Son(Father): # Single Level Inheritance
    def car(self):
        print("Has Car")
        
son_object = Son()
son_object.car()
son_object.house()

print("=" * 50)

# Multi Level Inheritance: GrandParent -> Parent -> Child 

class GrandFather:
    def land(self):
        print("Has Land")
        
class Father(GrandFather):
    def house(self):
        print("Has House")
        
class Son(Father): # Multi Level Inheritance
    def car(self):
        print("Has Car")
        
son_object = Son()
son_object.car()
son_object.house()
son_object.land()

print("=" * 50)

# Multiple Inheritance: One Child -> Multiple Parents 
#       Father | Mother
#            Child

class Father:
    def house(self):
        print("Has House")

class Mother:
    def gold(self):
        print("Has Gold")
        
class Son(Father,Mother): # Multiple Inheritance
    def car(self):
        print("Has Car")
        
son_object = Son()
son_object.car()
son_object.house()
son_object.gold()

print("=" * 50)

# Hierarchical Inheritance: One Parent -> Multiple Child 
#           Parent
#             |
#       Son       Daughter        
class Father:
    def house(self):
        print("Has House")
        
class Son(Father): 
    def car(self):
        print("Has Car")
        
class Daughter(Father): 
    def business(self):
        print("Has Business")
        
son_object = Son()
son_object.car()
son_object.house()

daughter_object = Daughter()
daughter_object.business()
daughter_object.house()

print("=" * 50)

# Hybrid Inheritance: Combination 
class A:
    def a(self):
        print("A Feature")
        
class B(A):
    def b(self):
        print("B Feature")

class C(A):
    def c(self):
        print("C Feature")
        
class D(B,C):
    def d(self):
        print("D Feature")
        
object_d = D()
object_d.a()
object_d.b()
object_d.c()
object_d.d()