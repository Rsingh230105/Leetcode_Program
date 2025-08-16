'''n=int(input("enter number:"))
l=[]
for i in range(1,n+1):# TC=o(n): all number iterate one by one  like 1 to n , sc=o(k), k is total number of factor
    if n%i==0:#tc=o(1)
        l.append(i)# tc=o(1)

print(l)'''

## optimal solution
#10 ->1,2,3,4,5,6,7,8,9,10
# jho no. hota hai uske aadhe bag ke number hi divide karte hai uss number ko like(1 to 5 ke bich ke) or last vo kud number like 10
# hame kewal number/2 hi iterate karana hai or uss kud no. ko
'''
n=int(input("enter number:"))
num=n
l=[]
for i in range(1,num//2):# TC=o(N/2) or remove constant, so o(N), SC=o(k)
    if n%i==0:
     l.append(i)
l.append(num)
print(l)
'''
###method 3###full optimal
from math import sqrt
n=int(input("enter number:"))
num=n
r=[]
for i in range(1,int(sqrt(num))+1): # TC=o(sqrt(N)), SC=o(k)
    if num%i==0:
        r.append(i)
        if num//i!=i:
            r.append(num//i)
print(r)

