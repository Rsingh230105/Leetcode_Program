#1.
a=~~~~~~5
print(a)
#2.
string = "my name is x"
for i in string.split():
    print (i, end=", ")

#3.
a = [10, 23, 56, [78]]
b = list(a)
print(b)
a[3][0] = 95
print(a)
print(b)
a[1] = 34
print(b)

#7.
x=12
def f1(a,b=x):
    print(a,b)
x=15
f1(4)