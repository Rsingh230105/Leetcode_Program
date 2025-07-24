#2.Write a program to check whether a number is a palindrome.
n=int(input("Enter the number:"))
original=n
reverse=0

while n>0:
    digit=n%10
    reverse=reverse * 10 + digit
    n=n//10

if original == reverse:
    print("palindrom number")
else:
    print("not palindrom number")
