#Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val:int):
        self.val = val
        self.next = None



class Solution:
    def TwoSum(self, l1: Optional[ListNode], l2: Optional[ListNode])->Optional[ListNode]:
        current1 = l1
        current2 = l2
        mylist1 = []
        mylist2 = []
        while current1.next is not None:
            mylist1.append(current1.val)
            current1 = current1.next
        mylist1.append(current1)

        while current2.next is not None:
            mylist2.append(current2.val)
            current2 = current2.next
        mylist1.append(current2)
        import math

# l1 = [1,2,3,4,9,4,6]
# power = len(l1)-1
# result = 0
# for c in l1:
#     c = c * math.pow(10,power)
#     result = result + c
#     power-=1
# print(result)


        return mylist1

o = Solution()
o.TwoSum([1,2,3,4,4],[2,3,4,5,5,6,5])
print(o)