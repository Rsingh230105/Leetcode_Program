class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        v = {}#this is dictionary
        i = 0
        r = 0
        for j in range(len(s)):
            if s[j] in v:
                i = max(v[s[j]], i)

            r = max(j - i + 1, r)
            v[s[j]] = j + 1
        print(r)
obj=Solution()
obj.lengthOfLongestSubstring("abcabcbb")
obj.lengthOfLongestSubstring("bbbbb")
obj.lengthOfLongestSubstring("pwwkew")