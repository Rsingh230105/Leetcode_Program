#1.
from pyexpat.errors import messages

name="shantanu"
print(name[2:8:-2])

#2
print("\\")# \
print("/\\/\\/\\/\\")# /\/\/\/\
# print("/\/\/\/\")

#3
print(2**3**2)#512

#4
print(-10//3)#-4
print(10//3)#3
print(10.0//3)# 3.0 , float ko divide karne per ya float se divide kare per float hi milega

#5
d={"jay":89,"viru":53,'jay':67} #duplicate remove and last value consider
print(len(d))
print(d)
print(d.keys())
print(d.values())
print(d.items())

#6
a=[1,4,7]
b=[2,5,8]
c=[3,6,9]
x=zip(a,b,c) # return object
print(list(x)) # return merge list in tuple form

#7
num=2E3 #2*10**3=2000.0
num1=2e3
print(type(num)) ##float
print(type(num1))

#8
# for i in 765<1: #syntax error because for loop using iterator(list,tuple...) but yha condition di hai
#     print(i)

#9
name='swapnali'
name1='Swapnali'
print(name==name1)# yha bhi first character ka ord number compare hota hai
print(name>=name1) # because ascii number(ord numbeer)
print(ord('s'))#115
print(ord('S'))#83

#10
'''1. Unary
    2.Binay operator
    3.Ternary operator: python me exist nahi karta hai per short if_else ki madad se achieve kar sakte hai
            value_if_true if condition else value_if_false
                   |            |            |         
                operand1     op_d2        op_d3'''

age=20
messages="you can vote" if (age>=18) else "You can not vote"
print(messages)

##11
'''What is PEP8
--> Python Interprise Proposal
--> A document that provides guidelines and best practices on how to write Python code.
--> It was written in 2001 by guido van Rossum.
--> These guideline are helpful to enhance the readability and consistency of programs.'''




