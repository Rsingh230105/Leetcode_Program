class Solution:
    def merge(self, nums1, m, nums2, n) :
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        print(nums1.sort())

obj=Solution()
obj.merge([1,2,3,0,0,0],3,[2,5,6],3)