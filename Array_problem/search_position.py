class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            for i in nums:
                if i == target:
                    print(nums.index(i))
                    return
        else:
            for j in nums:
                if j > target:
                    print(nums.index(j))
                    return
            # If target is greater than all elements
            print(len(nums))


obj = Solution()
obj.searchInsert([1, 3, 5, 7], 5)  # 2
obj.searchInsert([1, 3, 5, 6], 7)  # 4
obj.searchInsert([1, 3, 5, 6], 0)  # 0
