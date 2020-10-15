from copy import deepcopy
tuple1 = (1, 2, 3)
print(tuple1)
tuple2 = (1, "hi", [], 6.8)
print(tuple2)
print(tuple1[0])
tuplePacking = (4,5,6)
a, b, c = tuplePacking
print(a)
tupleString="a,b,c,d,e"
str= ''.join(tupleString)
print(tupleString)
print(tupleString[4])
tupleColon=("hi","how","are","you","today")
print (tupleColon)
tupleRepeat = (1, 2, 3, 2, 4, 3)
count = tupleRepeat.count(3)
print(count)
tupleCopy = deepcopy(tuple2)
tupleCopy[2].append(50)
print (tupleCopy)


thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
if ("banana" in thisset):
    thisset.add("orange")
elif ("cherry" in thisset):
    thisset.update("mango", "berries")
for x in thisset:
    print(x)
