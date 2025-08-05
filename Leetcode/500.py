class Solution:
    def findWords(self, words) :
        l1=set("qwertyuiop")
        l2=set("asdfghjkl")
        l3=set("zxcvbnm")
        op=[]
        for i in words:
            w=set(i.lower())
            if w<=l1 or w<=l2 or w<=l3:## this is two set comparison using <= operator this operator is find to w is sunset of l1(w ke set ke element l1 me hai ya nahi)
                op.append(i)
        print(op)


obj=Solution()
obj.findWords(["Hello","Alaska","Dad","Peace"])