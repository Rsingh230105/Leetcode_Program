#inheritance ka use karke hume har class ka object nahi banana padta hai child ke object se call kar sakte hai.
#1.single inheritance
#2.multiple
#3.multilevel

#1.single inheritance
class A:
    def display1(self):
        print("class A called")

class B(A):
    def display2(self):
        print("class B called")

obj=B()
obj.display1()
obj.display2()

#2.multilevel inheritance
class A:
    def display1(self):
        print("class A called")

class B(A):
    def display2(self):
        print("class B called")

class C(B):
    def display3(self):
        print("class C called,Multilevel inheritance")

obj=C()
obj.display1()
obj.display2()
obj.display3()

#3.multiple inheritance

class A:
    def display1(self):
        print("class A called")

class B:
    def display2(self):
        print("class B called")

class C(A,B):
    def display3(self):
        print("Multiple inheritance")

obj=C()
obj.display1()
obj.display2()
obj.display3()
