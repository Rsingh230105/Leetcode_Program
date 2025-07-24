#method ko object ke through call karna padta hai
#constructor ko call nahi karna padta vo object create hote hi call ho jata hai
class Demo:
    a=20
    def __init__(self):  #constructor
        print("constructor called")

    def show(self):
        self.c=self.a*self.a
        print(self.c)

    def show1(self,a,b):
        print(a+b)
        
obj=Demo()
obj.show()
obj.show1(45,55)
