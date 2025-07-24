#1.
'''
a=10
b=20
def change():
    global b
    a=45
    b=56
change()
print(a)
print(b)
#2.
print("ccdcddcd".find("c"))# return index no. first occurence

#3.
a=(1,2,3)
b=('A','B','C')
c=tuple(zip(a,b))
print(c)

#4
class tester:
    def __init__(self, id):
        self.id = str(id)
        id="224"

temp = tester(12)
print(temp.id)
'''
#5.
import turtle
t=turtle.Pen()
t.goto(300,9)
print(t.position())

#6.
def sum(*args):
   '''Function returns the sum of all values'''
   r = 0
   for i in args:
      r += i
   return r
print(sum.__doc__)
print(sum(1, 2, 3))
print(sum(1, 2, 3, 4, 5))

#7.
print([i.lower() for i in "HELLO"])

#8.
def f(x, y, z): return x + y + z
print(f(2, 30, 400))
#9.
print('Ab!2'.swapcase())

#10.
try:
    print("Do something")
except:
    print("kuch nahi")
else:
    print("Else bhi laga sakte hai")

#11.
    print(hex(15))#return hexadecimal in lowercase