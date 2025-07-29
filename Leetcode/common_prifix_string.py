class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        # Take the smallest and largest string (lexicographically)
        smallest = min(strs)
        print(smallest)
        largest = max(strs)
        print(largest)

        # Compare characters between smallest and largest
        prefix = ""
        for i in range(len(smallest)):
            if smallest[i] == largest[i]:
                prefix += smallest[i]
            else:
                break
        return prefix


# Test
obj = Solution()
print(obj.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
