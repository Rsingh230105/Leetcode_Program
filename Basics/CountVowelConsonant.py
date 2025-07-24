s=str(input("Enter the string:"))
count=0
if  "a,e,i,o,u,A,E,I,O,U" in s:
    for i in range(0,len(s)+1):
     count += 1
    print(s,count,end='')
else:
    print(s,count,end='')

