

#1.Write a program to calculate the sum of digits of a number.
n=int(input("Enter the number:"))
length=len(str(n))
print(length)

sum =0

while n>0:
    digit=n%10  #last digit
    sum=sum+digit
    n=n//10 # last digit hatata hai

print("Sum of digits :" , sum)

