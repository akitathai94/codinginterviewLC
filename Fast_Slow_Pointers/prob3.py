"""
Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.

If the total number of nodes in the LinkedList is even, return the second middle node.
"""
# Samples 
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
# Output: 3

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def find_middle(head):
    slo, fas = head, head
    while fas != None and fas.next != None:
        slo = slo.next
        fas = fas.next.next
    return slo


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)

print(find_middle(head).value)