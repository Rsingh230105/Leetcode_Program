class Solution:
    def thirdMax(self, nums):
        # Remove duplicates
        nums = list(set(nums))
        # Sort in descending order
        nums.sort(reverse=True)

        # If we have at least 3 distinct numbers, return the 3rd max
        if len(nums) >= 3:
            return nums[2]
        # Otherwise, return the maximum
        else:
            return nums[0]


# Test
obj = Solution()
print(obj.thirdMax([3, 2, 1]))  # Output: 1 (third maximum)
print(obj.thirdMax([1, 2]))  # Output: 2 (since only two numbers)
print(obj.thirdMax([2, 2, 3, 1]))  # Output: 1 (third distinct maximum)
