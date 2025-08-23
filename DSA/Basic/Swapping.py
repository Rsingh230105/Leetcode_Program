#method one
a=10
b=20
a,b=b,a
print("a",a)
print("b",b)
print()

##method2 temprary variable
a1=10
b1=20
temp=a1
a1=b1
b1=temp

print("a1:",a1)
print("b1:",b1)
print()
####method third

a2=10
b2=20

a2=a2+b2 ##a2=10+20=30
b2=a2-b2 ##b2=30-20=10
a2=a2-b2 ## a2=30-10=20
print("a2:",a2)
print("b2:",b2)



