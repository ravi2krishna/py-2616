# Dictionary Methods / Operations 
data = {"a":"apple","b":"banana"}
print(type(data))

# update(): Add / Update Item in dictionary
print(data)
data.update({"c":"cherry"}) # if key is not present, then add the item
print(data)

data.update({"a":"apricot"}) # if key is present, then update the item
print(data)

# pop(): Remove Item By Key
data = {"a":"apple","b":"banana"}
print(data)
data.pop("a")
print(data)

# popitem(): Remove Last Item 
data = {"a":"apple","b":"banana"}
print(data)
data.popitem()
print(data)

# clear(): Empties Dictionary
data = {"a":"apple","b":"banana"}
print(data)
data.clear()
print(data)

# get(): Used to get value for key 
data = {"a":"apple","b":"banana"}
print(data)
data.get("a")
print(data.get("a"))
print(data["a"])
# print(data["c"]) # KeyError: 'c'
print(data.get("c"))

# keys(): Used To Get Keys 
data = {"a":"apple","b":"banana"}
print(data)
data.keys()
print(data.keys())

for key in data.keys():
    print(key)
    

# values(): Used To Get Values 
data = {"a":"apple","b":"banana"}
print(data)
data.values()
print(data.values())

for value in data.values():
    print(value)
    
# items(): Used To Gets Item i.e Key & Value both
data = {"a":"apple","b":"banana"}
print(data)
data.items()
print(data.items())

for item in data.items():
    print(item)
    
# setdefault(): returns a value of key, if the key is already present
# if key is not present, then adds the item and then returns the value 
data = {"a":"apple","b":"banana"}
print(data)     

data.setdefault("b","blueberry")
print(data.setdefault("b","blueberry"))

data = {"a":"apple","b":"banana"}
print(data) 
print(data.setdefault("c","cherry"))
print(data) 

# copy(): Copies Dictionary
data = {"a":"apple","b":"banana"}
print(data) 
backup = data.copy()
print(backup)