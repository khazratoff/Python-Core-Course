# Definition for singly-linked list.






class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.headval = None

class Solution:
    def mergeTwoLists(self):
        Llist = LinkedList()
        Llist.headval = ListNode(None,None)
        node1 = ListNode(100)
        Llist.headval.next = node1 
        node2 = ListNode(200)
        node1.next = node2
        print(node2.val)
        


o = Solution()
o.mergeTwoLists()
