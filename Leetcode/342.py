class Solution:
    def isPowerOfFour(self,n) :
        if n <= 0:
            return False

        while n % 4 == 0:
            n = n // 4

        return n == 1

obj=Solution()
print(obj.isPowerOfFour(5))
print(obj.isPowerOfFour(-2113348))
print(obj.isPowerOfFour(1))
print(obj.isPowerOfFour(125))