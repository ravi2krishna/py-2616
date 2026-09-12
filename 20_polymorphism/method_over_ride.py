# Method Overriding --> provides a new implementation of a method that already exists in parent class

class Animal:
    
    def sound(self):
        print("Animal Makes Sound")
        
class Dog(Animal):
    
    def sound(self):
        print("Dog Makes Sound - Woof")
        
class Cat(Animal):
    
    def sound(self):
        print("Cat Makes Sound - Meow")
        
animal = Animal()
animal.sound()

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()