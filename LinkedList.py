

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.last = None


linked1 = SinglyLinkedList()
linked1.last = Node(9)
node1 = Node(3)
node2 = Node(5)
linked1.last.next = node1
node1.next = node2
node2.next = linked1.last

linked2 = SinglyLinkedList()
linked2.last = Node(99)
node3 = Node(33)
node4 = Node(55)
linked2.last.next = node3
node3.next = node4
node4.next = linked2.last

print(linked1.last.val, node1.val, node2.val)
print(linked2.last.val, node3.val, node4.val)

temp = linked2.last 
temp.next = node1
linked1.last = node3


print( node1.val, node2.val,linked1.last.val, node3.val, node4.val ) 