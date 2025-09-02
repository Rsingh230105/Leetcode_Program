nums=[1,7,8,4,5,6,9,2]
n=len(nums)
for i in range(n):
    for j in range(i+1,n):
        if nums[j]<nums[i]:## increasing order
            nums[j],nums[i]=nums[i],nums[j]

print(nums)
##TC=o(N^2)
##SC=O(1)


###desending
nums=[1,7,8,4,5,6,9,2]
n=len(nums)
for i in range(n):
    for j in range(i+1,n):
        if nums[j]>nums[i]: ## decreasing order
            nums[j],nums[i]=nums[i],nums[j]

print(nums)## decending order
