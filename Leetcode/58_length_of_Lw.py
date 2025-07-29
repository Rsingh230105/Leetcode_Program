class Solution:
    def lengthOfLastWord(self, s: str) -> int:
      x=s.split()
      print(x)
      l=len(x)
      print(len(x[l-1]))


obj=Solution()
obj.lengthOfLastWord("Hello World")