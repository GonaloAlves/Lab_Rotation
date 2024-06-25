"""
a = 100
b = 200

aList = list(range(a))
bList = list(range(b))
cList = [item for item in bList if item not in aList]
print (cList)

oddnumbersc = []
for item in cList:
  if item %2 != 0:
    oddnumbersc.append(item)    

print (oddnumbersc)    
"""



phones = {'Zoe':'232-43-58', 'Alice':'165-88-56'}
print (phones['Zoe'])

phones['Zoe'] = '658-99-55'
phones['Bill'] = '342-18-25'
print (phones)

d = {}
d['key'] = 1
d['Key'] = 2
d['KEY'] = 3
print (d)

if 'Peter' in phones:
    print ("We know Peter's phone")
else:
    print ("We don't know Peter's phone")

phones = {'Zoe':'232-43-58', 'Alice':'165-88-56'}
del phones['Zoe']
print (phones)


