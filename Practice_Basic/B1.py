l1=[1,2,3]
l2=[4,5,6]
print([x*y for x in l1 for y in l2])

for x in l1:
    for y in l2:
        print(x*y,end=" ")



