# With Abstraction

# There will Be Abstract Classes & Abstract Methods

# There will Be Contract Like Behaviors 

# Laptop Contract - Government said these 4 are must features for building Laptops 

# Concrete Class -> Abstract Class

# Abstract Class
from abc import ABC, abstractmethod 
class Laptop(ABC):
    
    # Concrete Methods -> Abstract Methods
    # Abstract Methods
    @abstractmethod
    def should_have_processor(self):
        pass
    
    @abstractmethod    
    def should_have_ram(self):
        pass 
    
    @abstractmethod     
    def should_have_hard_disk(self):
        pass
    
    @abstractmethod    
    def should_have_network(self):
        pass 