class Person:
    def __init__(self,name,age): # like constructor
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name}({self.age})"
    def getName(Self):
        return "My name is:",Self.name ,Self.age
p1=Person("Ram",22)
p2=Person("Radha",17)
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)
print(p1.getName())
print(p1)#without __str__ function returned object like (<__main__.Person object at 0x000002372B4E6E40>)





