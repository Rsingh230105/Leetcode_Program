# nums=[5,7,3,2,6,1,5,9]
# l=0
# r=len(nums)-1
# for i in range(l,r+1):
#     if l<r and l!=r:
#      nums[i],nums[r]=nums[r],nums[i]
#      l=l+1
#      r=r-1
#
# print(nums)

###Using recursion --> all array reverse and mid array reverse

def func(nums,l,r):
    if l>=r:
        return
    nums[l],nums[r]=nums[r],nums[l]
    func(nums,l+1,r-1)

def reverse(nums,l,r):
    func(nums,l,r)
    return nums
print(reverse([5,7,3,2,6,1,5,9],0,7))# all arraay reverse
print(reverse([5,7,3,2,6,1,5,9],2,5))# mid array reverse

