#dictionary me kitni list hai
data={'jay':['male',23,232323],'raj':25,'vicky':['male',22],'ram':['male',25]}
'''
isinstance(obj,list)-->ye true return karega yadi obj list hoga to
isinstance(obj,tuple)-->ye true return karega yadi  obj tuple hoga to
obj like: [1,2,3], (1,2,3).
'''
c=0
for i in data:
    if isinstance(data[i],list):
        print(i)
        print(data[i])
        c+=1

print(c)
