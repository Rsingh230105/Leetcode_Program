#1.function overloading

class A:
    def display(self,name=''):
        print("hiii",name)

obj=A()
obj.display()#no argument
obj.display('Python')# with argument

#2.function overriding
class A:
    def display(self):
        print("Parent called")
class B(A):
    def display(self):
        super().display() # function name same ho both class tab parent ke function ko call karne ke liye
        print("Child called")

obj=B()
obj.display()# only child called ,override parent without super keyword


class  Area:
    def find_area(self,x=None,y=None):
        if x!=None and y!=None:
            print(x*y)
        elif x!=None:
            print(x*x)
        else:
            print("Nothing")

obj=Area()
obj.find_area()
obj.find_area(10)
obj.find_area(10,20)