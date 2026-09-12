# Implementations -> Companies who wants to manufacture laptops 

# Dell Wants To Build Laptops 

from without_one import Laptop

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
    

# Without Abstraction - End User 

# End User Buying Dell Laptop
print("=" * 30)
print("     Customer Buying Dell Laptop")
print("=" * 30)

dell_object = Dell()
dell_object.should_have_processor()
dell_object.should_have_ram()