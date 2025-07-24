import CalculatorModule1 as c
print(c.sum(10,20))
print(c.mul(30,20))
print(c.sub(2,5))
'''
from CalculatorModule1 import sum #-->direct ek function call
print(sum(10,20))


from CalculatorModule1 import * # --> all function call/use
print(sum(11,22))
print(sub(11,22))
print(mul(11,22))

'''
