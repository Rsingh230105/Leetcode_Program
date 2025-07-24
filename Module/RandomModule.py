import random as r
n=r.randint(1,10)# both value included
print(n)

m=r.randrange(1,10)#1 include but 10 not included
print(m)

l=["Ram","hanuman","Krishna","Mahakal"]
print(r.choice(l))

fun=r.random()# 0 and 1 ke bich me koi bhi random value
print(fun)

fun1=r.uniform(1,10)# 1 and 10 ke bich me koi bhi float value dega
print(fun1)

l2=[10,20,30,40,50,60]
r.shuffle(l2)
print(l2)

