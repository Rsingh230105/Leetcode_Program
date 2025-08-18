x=str(input("enter the word:"))
v=['a','e','i','o','u','A','E','I','O','U'," "]
c=0
for i in x:
    print(i)
    if i in v:
        c+=1
print(c)
