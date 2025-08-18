'''
Walrus operator (:=)
-->You can assign a value within an expression
-->parenthese ke sath iss operator ka use kare
'''
#1
print((a := 100)+1)
#print(a=100+1)##error
##print((a=100)) #error

##2
while True:
    ans=input("Do you want to continue(y/n):").lower() #y
    if ans!='y':
        break
    print("process the request\n")

##3 Using walrus operator
while (ans:=input("Do you want to continue(y/n):").lower())=="y":
    print("process the request")
