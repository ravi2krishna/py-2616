# List Methods / Operations

# append(): Add Element To end of the list
data = [10,20,30,40,50]
print(data)
data.append(60)
print(data)

# extend(): Add Iterables To end of the list
data = [10,20,30,40,50]
print(data)
data.extend([60,70,80])
print(data)

# insert(): add element at specific index position
data = [10,20,40,50]
print(data)
data.append(30)
print(data)

data = [10,20,40,50]
print(data)
data.insert(2,30)
print(data)

# pop(): Remove element by default at last position
data = [10,20,30,40,50]
print(data)
data.pop()
print(data)

# remove 30
data = [10,20,30,40,50]
print(data)
data.pop(2)
print(data)

data = [10,20,30,40,50]
print(data)
# data.pop(20) # IndexError: pop index out of range
print(data)

# remove(): Remove element based on value
data = [10,20,30,40,50]
print(data)
data.remove(30)
print(data)

# clear(): Remove all elements and empty list 
data = [10,20,30,40,50]
print(data)
data.clear()
print(data)

# index(): Gives Index Position Of Value
data = [10,20,30,40,50]
print(data)
data.index(40)
print(data.index(40))
# print(data.index(400)) # ValueError: 400 is not in list

# count(): Return number of occurrences of value.
data = [10,20,30,40,50]
print(data)
data.count(10)
print(data.count(10))
data = [10,20,10,30,40,10,50]
print(data.count(10))

# reverse() - Reverses list 
data = [10,20,30,40,50]
print(data)
data.reverse()
print(data)

# sort(): Sort the list, default is ascending order 
data = [10,20,30,50,40]
print(data)
data.sort()
print(data)

data = [10,20,30,50,40]
print(data)
data.sort(reverse=True)
print(data)

# copy(): Creates Copy Of List 
data = [10,20,30,40,50]
print(data)
backup = data.copy()
print(backup)

# Employee PAN ID's
pan = ["ABCDE1234A","ABCDE1234B","ABCDE1234C","ABCDE1234D"]
print(pan[0])
# Test if id can be changed or not
pan[0] = "ABCDE1234Z"
print(pan[0]) # id is changed 