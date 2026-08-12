# Sets Methods / Operations 

# add(): add element to set 
data = {10,20,30,40,50}
print(data)
data.add(60)
print(data)

# update(): add multiple elements to set 
data = {10,20,30,40,50}
print(data)
data.update([60,70,70,80,90])
print(data)

# pop(): Removes Random Element 
data = {10,20,30,40,50}
print(data)
data.pop()
print(data)

# remove(): Removes Element By Value 
data = {10,20,30,40,50}
print(data)
data.remove(10)
# data.remove(100) # KeyError: 100
print(data)

# discard(): Removes Element By Value 
data = {10,20,30,40,50}
print(data)
data.discard(10)
data.discard(100) # KeyError: 100
print(data)

# clear(): Empties Set 
data = {10,20,30,40,50}
print(data)
data.clear()
print(data)
data.add(20)
print(data)

# copy(): Creates Copy 
data = {10,20,30,40,50}
print(data)
backup = data.copy()
print(backup)

 
