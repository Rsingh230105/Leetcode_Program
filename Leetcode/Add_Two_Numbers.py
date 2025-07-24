# Definition for singly-linked list.
class ListNode:
    def __init__(self):
        self.l1 = []
        self.l2 = []
        self.l3 = []

        for i in range(100):
            value = input()
            self.l1.append(value)
            print(self.l1)
        for i in range(100):
            value = input()
            self.l2.append(value)
            print(self.l2)
        for j in range(len(self.l1)):
            sum_val = self.l1[j] + self.l2[j]
            slist=self.l3.append(sum_val)
            print(slist)


