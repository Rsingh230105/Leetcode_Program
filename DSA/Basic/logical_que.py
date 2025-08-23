'''
input: a3b2c4
output: aaabbcccc
'''

# only correct string enter like a3h4j5 , not enter ee4t544yy, so this error
n=input("Enter the string:")
s=""

for j in range(0,len(n),2):
    s=s + n[j] * int(n[j+1])

print(s)

###all string consider and correct output
x=input("Enter the string:")
op=""

for i in x:
    if i.isalpha():
        var=i
    else:
        num=int(i)
        op=op+(var*num)
print(op)

