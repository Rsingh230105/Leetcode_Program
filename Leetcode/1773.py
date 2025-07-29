class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        count = 0
        for t, c, n in items:
            if ruleKey == "type" and ruleValue == t:
                count += 1
            elif ruleKey == "color" and ruleValue == c:
                count += 1
            elif ruleKey == "name" and ruleValue == n:
                count += 1
        return count

# Create the object
obj = Solution()

# Call with correct arguments
items_list = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
x = obj.countMatches(items_list, "type", "phone")     # Should return 2
y = obj.countMatches(items_list, "color", "silver")   # Should return 1
z = obj.countMatches(items_list, "name", "lenovo")    # Should return 1

print(x,y,z)
