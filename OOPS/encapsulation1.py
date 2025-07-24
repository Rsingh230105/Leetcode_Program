class Student:
    __name="RRRRR"
    def __init__(self):
        print(self.__name)
        self.__displayinfo()

    def __displayinfo(self):
        print("hello")
        
obj=Student()