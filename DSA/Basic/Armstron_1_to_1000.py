# l=[]
# for i in range(1,1001):
#     n=len(str(i))
#     if n>1000:
#         break
#     elif n==1:
#         l.append(i)
#     elif n==2:
#         i=str(i)
#         sum=int(i[0])**n + int(i[1])**n
#         if sum==int(i):
#             l.append(i)
#     elif n == 3:
#             i=str(i)
#             sum = int(i[0]) ** n + int(i[1]) ** n +int(i[2])**n
#             if sum == int(i):
#
#                 l.append(sum)
# print(l)
#
'''
##method2

for i in range(1,1001):
    num=i
    n=len(str(i))

    sum=0
    i=str(i)

    for digit in i:
        sum+=int(digit)**n
    if sum == num:
        print(num)
'''
### Using while loop
for i in range(1,1001):
    num=i
    n=len(str(i))
    sum=0

    while i!=0:
        ld=i%10 ##last digit
        sum = sum + ld ** n
        i=i//10 ## bache hue digit

    if sum == num :
        print(sum)



