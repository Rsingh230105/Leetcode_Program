class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        print(s)
        for i in range(0,len(s),2*k):
            print(i)
            s[i:i+k] = reversed(s[i:i+k])
            # print(s[i:i+k])
        print("".join(s))

obj=Solution()
obj.reverseStr("abcdefg",2)