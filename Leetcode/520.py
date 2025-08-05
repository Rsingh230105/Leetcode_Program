class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper():
            print(True)
        if word.islower():
            print(True)
        if word[0].isupper() and word[1:].islower():
            print(True)
        return False
obj=Solution()
obj.detectCapitalUse("USA")
obj.detectCapitalUse("g")
obj.detectCapitalUse("leetcode")
obj.detectCapitalUse("FlaG")#dout