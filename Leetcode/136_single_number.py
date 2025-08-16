#Optimal solution
'''
class Solution:
    def singleNumber(self, nums) :
        ans = 0
        for i in nums:
            ans ^= i #a^a=0,a^0=0 a convert binary than xor operation
        print(ans)

obj=Solution()
obj.singleNumber([1,2,1,3,3,3])
obj.singleNumber([4,1,2,1,2])
'''


## worst solution
class Solution:
    def singleNumber(self, nums) :
        for i in nums:
            if nums.count(i) == 1:
                print(i)

obj=Solution()
obj.singleNumber([1,2,1,3,3,3])
obj.singleNumber([4,1,2,1,2])