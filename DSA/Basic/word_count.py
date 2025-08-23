##method one
# text=input("enter your text:")
# n=int(input("enter your times:"))
#
# words=text.split()
# res=[]
#
# for word in words:
#     if words.count(word)>=n:
#         res.append(word)
# unique=set(res)
# print(list(unique))

##method2
text=input("enter your text:")
n=int(input("enter your times:"))

words=text.split()
d={}
l=[]

for i in words:
    if i in d:
        d[i]+=1
    else:
        d[i]=1


print(d)

for i in d:
    if d[i]>=n:
        l.append(i)

if len(l)>0:
    print(l)
else:
    print("NA")










