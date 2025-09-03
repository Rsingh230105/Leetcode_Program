##method1
##TC=o(n)
##SC=o(1)
nums=[55,32,-97,99,3,67]
largest=nums[0] ## if hum largest ko zero lenge to [-55,-44,-644] negative ko vo zero de dega isliye hum first element ko lete hai

for i in nums:
    if i>largest:
        largest = i

print(largest)

##method2
nums=[55,32,-97,99,3,67]
largest=float("-inf")##-infinity sabse small element

for i in nums:
    if i>largest:
        largest = i

print(largest)


###Second largest
#method1
nums=[55,32,97,-55,45,32,88,21]
nums.sort()
print(nums[-2])##second largest element
##TC=o(nlogn)
##SC=o(1)

##method2

nums=[55,32,97,-55,45,32,88,993,432,21]
largest=float("-inf")
#s_largest=float("-inf")

for i in nums:
    if i>largest:
        largest = i

nums.remove(largest)

s_largest=float("-inf")

for i in nums:
    if i>s_largest:
        s_largest = i

print(s_largest)##second largest element



#method 3
nums=[55,32,97,-55,45,32,88,993,432,21]
largest=float("-inf")
s_largest=float("-inf")
n=len(nums)
for i in range(0,n):
    largest=max(largest,nums[i])

for i in range(0,n):
    if nums[i]>s_largest and nums[i]!=largest:
        s_largest=nums[i]

print(s_largest)


##method4
##Optimal solution -->singal pass solution
##TC=o(n)
##Sc=o(1)

nums=[55,32,97,-55,45,32,88,993,432,21]
largest=float("-inf")
s_largest=float("-inf")
n=len(nums)

for i in range(0,n):
    if nums[i]>largest:
        s_largest=largest
        largest=nums[i]
    elif nums[i]>s_largest and nums[i]!=largest:
        s_largest=nums[i]

print(s_largest)

