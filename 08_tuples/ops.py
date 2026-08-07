# Tuples Methods / Operations

# index(): Gives Index Position Of Value
data = (10,20,30,40,50)
print(data)
data.index(40)
print(data.index(40))
# print(data.index(400)) # ValueError: 400 is not in list

# count(): Return number of occurrences of value.
data = (10,20,30,40,50)
print(data)
data.count(10)
print(data.count(10))
data = [10,20,10,30,40,10,50]
print(data.count(10))


# Employee PAN ID's
pan = ("ABCDE1234A","ABCDE1234B","ABCDE1234C","ABCDE1234D")
print(type(pan))
print(pan[0])
# Test if id can be changed or not
pan[0] = "ABCDE1234Z" # TypeError: 'tuple' object does not support item assignment
print(pan[0]) # id is changed 