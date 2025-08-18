##max
l=[1,4,3,6,9,20,56,34]
max=l[0]
for i in l:
    if max<i:
        max=i
print(max)

##min
l1=[17,4,3,6,9,20,56,34]
min=l1[0]
for i in l1:
    if min>i:
        min=i
print(min)

l.extend(l1)## multiple element ko append karne ke liye iss method ka use kiye jata hai
print(l)
print(l1)