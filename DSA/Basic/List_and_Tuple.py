"""
1.List:
-->a) List is a comma separated values in square brackets and square brackets is mandatory.
---> Data=['jay',23,40000404]

--->b)List is mutable
--->c)List is slow in execution than tuple
---->d)List is less efficient in memory utilization than tuple.
----> e)Comprehension concept is applicable only for list and not for tuple
--->f)List supports both Packing and unpacking -->chatgpt
2.Tuple:
--> Tuple is a comma seperated vakues in paranthesis and parenthesis is optional
-->d='jay',23,2000
--->d=('jay',23,40000404)

-->Tuple is immutable
--> Tuple object takes less memory than list object for same data.
--->Tuple support both packing and unpacking
"""
t='jay',23,40000404
t1='jay', #tupel
t2='jay'  #string
t3=450959 #int
print(t)
print(t1)
print(type(t))
print(type(t1))
print(type(t2))
print(type(t3))


##Size list and tupel
import sys
l=[1,2,3] #88 byte
t=(1,2,3) #64
l1=[5]
t1=(5)  #int
t2=(5,) #tuple

print(sys.getsizeof(l))#88
print(sys.getsizeof(t))#64
print(sys.getsizeof(l1))#64
print(sys.getsizeof(t1))#28
print(sys.getsizeof(t2))#48
print(type(t1))#int
print(type(t2))#tuple


####Packing & unpacking
a,b,c,g,h=[1,2,3,'helllo','12.3'] ##unpaking
x=[5,7,4,32.2,7]# packing
d,e,f=(1,2,3)
print(g)
print(d,e,f)
