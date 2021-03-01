from __future__ import print_function
"""
Reverse a single Linklist
"""
# Input: 2 -> 4 -> 6 -> 8 -> 10 -> NULL
# Output: 10 -> 8 -> 6 -> 4 -> 2 -> NULL

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ->", end =' ')
            temp = temp.next
        print("NULL")
        print()

def reverse(head):
    curr = head
    prev, ahead = None, None
    # link-list reversal 
    # get prev = None, curr = head, next = curr.next 
    # while curr:
    # curr.next = prev
    # prev = curr 
    # curr = next 
    # next = next.next
    while curr is not None:
        ahead = curr.next
        curr.next = prev
        prev = curr
        curr = ahead
    return prev

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse(head)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()