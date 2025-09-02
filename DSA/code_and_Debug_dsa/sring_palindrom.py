'''
s=input("Enter the string: ")
s1=""
for i in range(0,len(s)):
    s1=s[i]+s1
if s==s1:
    print("Given String is palindrom")
else:
    print("Given String is not palindrom")

##Using normal function
def func(s):
    if s==s[::-1]:
        return True
    else:
        return False
print(func("NITIN"))
'''
##using while loop

##TC=o(n)
##sc=o(1)
def func(s,left,right):
 while left<right:
    if s[left] != s[right]:
        return False
    left+=1
    right-=1
 return True

print(func("NITINBYY",0,7))

##Using recursion
#TC=o(n)
#sc=o(n) -->stack space

def func(s,l,r):
    if l>=r:
        return True
    if s[l]!=s[r]:
        return False
    return func(s,l+1,r-1)

print(func("NITIN",0,4))

