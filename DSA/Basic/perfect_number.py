##Perfect number:- positive integer that is equal to sum of its positive divisiors ,excluding the nuber itself.
##like: 6->1,2,3 and 6 divisor of six ,but not include 6
## so, 1+2+3=6, this is perfect number

n=int(input("enter the number:"))
sum=0
if n<0:
    print("the number is negative")

for i in range(1,n+1):
    if n%i==0 and n!=i:
        sum=sum+i

if sum==n:
    print("the number is perfect")
else:
    print("the number is not perfect")


