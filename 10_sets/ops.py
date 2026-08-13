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

# special methods specific to sets only 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}

# union(): Combines The Sets 
print(s1.union(s2))
print(s1 | s2)

# intersection(): Get Common Elements From Sets 
print(s1.intersection(s2))
print(s1 & s2)
print(s1)
print(s2)

# intersection_update(): Get Common Elements From Sets, Update Calling Set  
print(s1.intersection_update(s2))
print(s1)
print(s2)

# NOTE: Moving ahead all _update() methods does the same 

# difference(): Removes Common Elements From Set and Gives Unique Elements 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.difference(s2))
print(s2.difference(s1))

print(s1 - s2)

print(s1)
print(s2)

# difference_update(): Removes Common Elements From Set and Gives Unique Elements, Update Calling Set   
print(s1.difference_update(s2))
print(s1)
print(s2)

# symmetric_difference(): Removes Common Elements From Set and Take Combined Elements From Both Sets 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference(s2))
print(s1 ^ s2)

print(s1)
print(s2)

# symmetric_difference_update(): Removes Common Elements From Set and Take Combined Elements From Both Sets, Update Calling Set    

print(s1.symmetric_difference_update(s2))

print(s1)
print(s2)

# issubset(): Checks If Given Set is Subset of Another Set 
s1 = {10,20,30,40,50}
s2 = {60,70,80}
s3 = {40,50}

print(s2.issubset(s1))
print(s3.issubset(s1))

# issuperset(): Checks If Given Set is SuperSet of Another Set 
s1 = {10,20,30,40,50}
s2 = {60,70,80}
s3 = {40,50}

print(s1.issuperset(s2))
print(s1.issuperset(s3))

# isdisjoint(): Checks If Given Sets have no common elements 
s1 = {10,20,30,40,50}
s2 = {60,70,80}
s3 = {40,50}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))