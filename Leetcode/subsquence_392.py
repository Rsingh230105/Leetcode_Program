class Solution:
    def isSubsequence(self, s: str, t: str) :
        op = 0
        for char in t:
            if op < len(s) and s[op] == char:
                op = op + 1
        print(op == len(s))

obj=Solution()
obj.isSubsequence("abc","ahcxbdfc")
