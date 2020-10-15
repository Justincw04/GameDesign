#Justin Cortez Wartell
#Dictionary Work

y={4:40,2:20,1:10,3:30}
#ascending and decending
l=list(y.items())
l.sort()
print(l)

l=list(y.items())
l.sort(reverse=True)
print('Descending order is',l)


dict=dict(l)

#concetenating dictionaries
d1={1:2,3:4}
d2={5:6,7:9}

dall = {}
dall.update(d1)
dall.update(d2)

#check if there is a key (not working)
print(dall)

if '17' in y:
  print ("yes")
else:
  print ("no")

#for loop corresponds
d = {'Red': 1, 'Green': 2, 'Blue': 3}
for color_key, value in d.items():
     print(color_key, 'corresponds to ', d[color_key])
#squares
del(dict)

s=dict()
for x in range(1,16):
    s[x]=x**2
print(s)


#merging
dictA = {'a': 10, 'b': 8}
dictB = {'d': 6, 'c': 4}

def Merge(dictA, dictB):
    return(dictB.update(dictA))

print(Merge(dictA, dictB))
print(dictB)
