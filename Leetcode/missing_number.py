class Solution:
    def missingNumber(self, nums) :
        maximum = max(nums)

        for i in range(0, maximum + 1):
            if i in nums:
                pass
            else:
                return i

        return maximum + 1

obj= Solution()
print(obj.missingNumber([1,0,3,2,4,5,8,7]))