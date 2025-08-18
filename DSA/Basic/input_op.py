#1
s="Sky is blue" ##o/p=blue is Sky
l=s.split()
rev=l[::-1]
op=" ".join(rev)
print(op)

#mehod2
# for i in rev:
#     print(i,end=" ")
print()
print()

#2
l=[1,2,2,3,3,4,5,5,5,6,6]
l1=[]
# for i in l:
#     if l.count(i)==1:
#         l1.append(i)
# print(l1)
##
print([i for i in l if l.count(i)==1])
##method 2

##3
s="a,a,a,b,b,c,c,c" # op=a:3,b:2,c:3
l=s.split(',')
print(l)
d={}
for i in range(0,len(l)):
    if l[i] in d:
        d[l[i]]+=1
    else:
        d[l[i]]=1
print(d)   

