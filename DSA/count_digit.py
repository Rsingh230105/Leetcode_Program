n=int(input("Enter a number:"))
c=0
while n>0:
    # last_digit=n%10
    # print(last_digit)
    #Space compexity:o(1)
    n=n//10# remove last digit # Time compexity = o(log_base_10(N)) if n//5 hota  to (log_base_5(N)) hota N=number
    c=c+1
print("total_digit",c)
