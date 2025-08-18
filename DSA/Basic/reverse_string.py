x="python is easy"
l=x.split()
l1=[]
print(l)
for i in l:
    l1.append(i[::-1])
print(l1)

op=" ".join(l1)
print(op)