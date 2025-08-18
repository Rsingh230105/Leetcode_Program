l=["hello",10,20,40,20,60,40,30]
l1=[]
for i in l:
    if l.count(i)>1 and i not in l1:
        l1.append(i)

#print(set(l1))
print(l1)

## without buit in method
l2=["hello",10,20,40,20,60,40,30]
d=[]
for i in range(len(l2)):
    for j in range(i+1,len(l2)):
        if l2[i]==l2[j] and l2[i] not in d:
            d.append(l2[i])
print(d)
