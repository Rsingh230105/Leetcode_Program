class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum=0
        self.a=a
        self.b=b
        for i in a:
            for j in b:
                sum=a[i]+b[j]

        return sum



obj=Solution()
obj.addBinary("1010","1011")