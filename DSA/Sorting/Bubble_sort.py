nums=[5,8,1,6,9,2,4]
n=len(nums)
for i in range(n-2,-1,-1):
    for j in range(0,i+1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]

print(nums)

##TC=o(N^2)--> worst and average
##SC=o(1)

## Best case if sorted ho
## best case complexity --> o(N)
nums=[1,2,3,4,5,6,7,8]
n=len(nums)
is_swapped=False
for i in range(n-2,-1,-1):
    for j in range(0,i+1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
            is_swapped=True
    if is_swapped == False:
        break

print(nums)