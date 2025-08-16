n=int(input("enter number: "))
num=n
result=0
nod=len(str(n))

while num>0:
    last_digit=num%10
    result=result+last_digit ** nod
    num=num//10                         # TC=o(log_base_10(N))  , Sc=

print(f"{n} is armstrong number:",result==n)


#type2
'''def isArmstrong(n):
    num = n
    result = 0
    nod = len(str(n))
    while num>0:
     last_digit=num%10
     result=result+last_digit ** nod
     num=num//10
    print(result==n)

isArmstrong(153)'''
