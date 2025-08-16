n=int(input("Enter a number: "))
num=n
rev=0
while num>0:
    last_digit=num%10
    rev=rev*10+last_digit
    num=num//10#   TC=o(log_base_10(N)), SC=o(1)
if n==rev:
    print(f"{n} number is palindrome")
else:
    print(f"{n} number is not palindrome")
