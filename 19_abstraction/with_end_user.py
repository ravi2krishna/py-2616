# Without Abstraction - End User 
from with_two import Dell

# End User Buying Dell Laptop
print("=" * 30)
print("     Customer Buying Dell Laptop")
print("=" * 30)

dell_object = Dell()
dell_object.should_have_processor()
dell_object.should_have_ram()
dell_object.should_have_hard_disk()
dell_object.should_have_network()


# atm_object = ATM()
# atm_object.check_balance()
# atm_object.withdraw()
# atm_object.get_statement()
# atm_object.change_pin()