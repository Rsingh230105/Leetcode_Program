## Twin prime number jisme difference two ka hota hai
## 11 and 13 are twin prime number => 13-11=2


num1=int(input("enter first number:"))
num2=int(input("enter second number:"))

def IsPrime(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

if IsPrime(num1) and IsPrime(num2):
    if abs(num1-num2)==2:
        print("both twin prime numbers")
    else:
        print("only two prime numbers")
else:
    print("numbers are not prime")

IsPrime(num1)
IsPrime(num2)









