class Solution:
    def removeElement(self, nums, val) :
        c = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[c] = nums[i]
                c += 1
        print(c)

obj=Solution()
obj.removeElement([3,2,2,3],3)