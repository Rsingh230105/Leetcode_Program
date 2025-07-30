class Solution:
    def isPalindrome(self, s: str):
        op=""
        l = s.lower()
        for i in l:
            if i.isalnum():# sirf alphabet or numbers rakhenge
                op=op+i
        return op==op[::-1]





obj=Solution()
obj.isPalindrome("A man, a plan, a canal: Panama")