
#1.Write a program to print "Hello, World!"
#print("Hello World")
'''
#2.Write a program to add two numbers entered by the user.
a=int(input())
b=int(input())
c=a+b
print("Add a and b is:",c)

#3.Write a program to check whether a number is even or odd.
print("Enter the number: ")
n=int(input())
if n%2==0:
    print("Even")
else:
    print("odd")

#4.Write a program to calculate the factorial of a number
n=int(input("Enter the number:"))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i

print("factorial "+ str(n)+" is:",factorial)

5.
n=int(input("Enter the number:"))
for i in range(1,11):
    table=n*i
    print(str(n)+ "*"+str(i)+" =",table)
6.
n=int(input("Enter the position of Fibonacci number:"))
a=0
b=1
for i in range(2,n):
    temp=a+b
    a=b
    b=temp
print("Fibonacci  number is:", temp)

#7.Write a program to check whether a number is prime or not.

n=int(input("Enter the number:"))
count=0

for i in range(1,n+1):
        if n%i==0:
            count += 1

if count==2:
    print("Prime number")
else:
    print("Not prime number")


#8.Write a program to reverse a string entered by the user
s=str(input("Enter the string:"))
print(s[::-1])


#9.Write a program to find the largest among three numbers.
a=int(input("Enter the first  number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the Third number:"))

if a>b :
    if a>c:
     print("a is greater")
elif b>c:
    if b>a:
     print("b is greater")
else:
    print("c is greater")

'''

#10.Write a program to create a simple calculator (add, subtract, multiply, divide).

a=int(input("Enter the first  number:"))
b=int(input("Enter the second number:"))

add=a+b
sub=a-b
mul=a*b
div=a/b
mod=a%b

op=str(input("Enter operation: (add,sub,mul,div,mod): "))

if op=="add":
    print(f"The sum of {a} and {b}",add)
elif op=="sub":
    print(f"The difference of {a} and {b}: ",sub)
elif op == "mul":
    print(f"The multiplication of {a} is {b}: ", mul)
elif op == "div":
    print(f"The divided of {a} is {b}: ", div)
elif op == "mod":
    print(f"The remainder of {a} is {b}: ", mod)
else:
    print("invalided input")


str="durga"
print("hiiiiii",str[1:9])

a=1000000000040400404040404040404040404040040404040040
b=20.454345433434343334343444
print(type(a))
print(type(b))


