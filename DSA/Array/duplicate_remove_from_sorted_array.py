nums=[1,1,1,2,3,4,4,7,9,9,9,10]##inplace
l=[]

for i in range(0,len(nums)):
    if nums[i] not in l:
        l.append(nums[i])

print(len(l))

##method 2
nums=[1,1,1,2,3,4,4,7,9,9,9,10]##inplace
d={}
for i in range(0,len(nums)):
    if nums[i] not in d:
        d[nums[i]]=1
    else:
        d[nums[i]]+=1

print(d)
k=list(d.keys())
print(k)##only contain unique value and maintain order

##method 3
##TC=o(2n) or o(n)
##SC=o(N)
nums=[1,1,1,2,3,4,4,7,9,9,9,10]##inplace
d={}
for i in range(0,len(nums)):
        d[nums[i]]=0
j=0
for num in k:
    nums[j]=num
    j+=1
print(j)

##method4
##optimal
##TC=o(n)
##SC=o(1)
nums=[1,1,1,2,3,4,4,7,9,9,9,10]##inplace
n=len(nums)

if n==1:
    print(1)
i=0
j=i+1

while j<n:
    if nums[i]!=nums[j]:
        i+=1
        nums[i],nums[j]=nums[j],nums[i]
    j+=1
print("optimal unique element of total number :",i+1)
