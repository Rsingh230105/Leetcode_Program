nums=[1,2,6,7,9,11,20]
n=len(nums)

is_sorted = True
for i in range(0,n-1):
    if nums[i]>nums[i+1]:
        is_sorted = False
        break

print(is_sorted)

##TC=o(n)
##SC=o(1)