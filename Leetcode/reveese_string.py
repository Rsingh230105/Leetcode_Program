class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        # rev=s[::-1]
        rev=s.reverse()
        print(rev)
obj=Solution()
obj.reverseString(["h","e","l","l","0"])