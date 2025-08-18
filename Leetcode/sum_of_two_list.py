class Solution:
    def findRestaurant(self, list1, list2):
        d2 = {}
        l = []
        for i in range(len(list2)):
            d2[list2[i]] = i
        for i in range(len(list1)):
            if list1[i] in d2:
                l.append([i + d2[list1[i]], list1[i]])
        l1 = []
        l.sort()
        l1.append(l[0][1])
        for i in range(1, len(l)):
            if l[i][0] == l[i - 1][0]:
                l1.append(l[i][1])
            else:
                break
        return l1


obj=Solution()
print(obj.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))
