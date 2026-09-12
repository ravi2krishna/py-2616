# Implementations -> Companies who wants to manufacture laptops 

# Dell Wants To Build Laptops 

from with_one import Laptop

class Dell(Laptop):
    
    def should_have_processor(self):
        print("=" * 30)
        print("Dell")
        print("=" * 30)
        
        print("Laptop")
        print("Processor")
        print("Functionality")
        print("Present")
        
    def should_have_ram(self):
        print("=" * 30)
        print("Dell")
        print("=" * 30)
        
        print("Laptop")
        print("RAM")
        print("Functionality")
        print("Present")
        
    # NOTE: Dell doesn't have Hard Disk and Wi-fi Network, 
    # but still able to sell the Laptops Without Any Contract Binding 
    
    # TypeError: Can't instantiate abstract class Dell without an implementation for 
    # abstract methods 'should_have_hard_disk', 'should_have_network'

    # Now Dell Is Forced To Bind By All Contracts Given 
    
         
    def should_have_hard_disk(self):
        print("=" * 30)
        print("Dell")
        print("=" * 30)
                
        print("Laptop")
        print("HARD DISK")
        print("Functionality")
        print("Present")
        
    
    def should_have_network(self):
        print("=" * 30)
        print("Dell")
        print("=" * 30)
                        
        print("Laptop")
        print("WIFI Network")
        print("Functionality")
        print("Present") 
        
    # Now Dell Should Be Selling Laptops