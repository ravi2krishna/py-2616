# Check API and Process 

# response = requests.get('https://dummyjson.com/products') # NameError: name 'requests' is not defined
# status_code = response.status_code
# print(status_code)

# import requests # ModuleNotFoundError: No module named 'requests'
# response = requests.get('https://dummyjson.com/products') # NameError: name 'requests' is not defined
# status_code = response.status_code
# print(status_code)

# pip install requests (Run in terminal)
import requests 
response = requests.get('https://dummyjson.com/products') 
status_code = response.status_code
print(status_code)
if status_code == 200:
    print("Processing Products API")
else:
    print("Processing Products API Failed")
print("=" * 10)

response = requests.get('https://dummyjson.com/countries') 
status_code = response.status_code
if status_code == 200:
    print("Processing Countries API")
else:
    print("Processing Countries API Failed")
print(status_code)

print("=" * 10)