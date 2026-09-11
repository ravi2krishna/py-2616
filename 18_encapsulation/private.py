# Private Access 

class A:
    def __init__(self,a):
        self.__a = a # Private i.e prefixed with a double underscore (__)
        
obj = A(10)

# Python = “You shouldn’t, but you can if you insist”
# print(obj._MyClass__private_variable) 
# print(obj.a) # AttributeError: 'A' object has no attribute 'a'
# print(obj._A__a) 

# Real World Use Case 
class CreditCardPayment:
    def __init__(self,card_number,card_cvv):
        self.card_number = card_number # This is not encapsulated
        self.__card_number = card_number
        self.__card_cvv = card_cvv
