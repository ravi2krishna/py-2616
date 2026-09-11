# Private Access 

class A:
    def __init__(self,a):
        self.__a = a # Private i.e prefixed with a double underscore (__)

class B(A):
    def showA(self):
        a = A(10)
        print(a.__a)

# obj = B(100)
# obj.showA()

# obj = A(10) # Outside

# Protected Access 
class A:
    def __init__(self,a):
        self._a = a # Protected i.e prefixed with a single underscore (_)

class B(A):
    def showA(self):
        a = A(10)
        print(a._a)

obj = B(100)
obj.showA()