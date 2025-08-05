class Solution:
    def plusOne(self, digits):
        op = ""
        l = []


        for i in digits:
            op = op + str(i)

        j = int(op) + 1
        k = str(j)

        for m in k:
            l.append(int(m))

        print(l)

obj=Solution()
obj.plusOne([1,2,3])


