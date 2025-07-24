class student:
    def __init__(self):
        self.__name=""  #__name ek private variable hai
    def getname(self):
        return self.__name

    def setname(self,name):
        self.__name=name

obj=student()
obj.setname("Testing")
name=obj.getname()
print(name)