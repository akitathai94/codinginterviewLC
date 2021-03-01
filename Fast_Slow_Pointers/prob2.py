"""
Given the head of a Singly LinkedList that contains a cycle, 
write a function to find the starting node of the cycle.
"""
from __future__ import print_function

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end= '')
            temp = temp.next
        print()

def find_cycle_start(head):
    # Data structure/ Algo from characteristic problems? Find start node of a cycle
    # Generate samples / How pattern samples look like? 
    # From every substep, go back to step 1 to see if we can optimize from it.

    # First find the length of the cycle by implement slo and fast ptr
    slo, fas = head, head
    length = 0
    ptr1, ptr2 = head, head
    while fas != None and fas.next != None:
        fas = fas.next.next
        slo = slo.next
        if fas == slo:
            length = get_length_cycle(slo)
            i = 1           
            # Traverse the pointer2 length node
            while i <= length:
                ptr2 = ptr2.next
                i += 1
            # then two ptrs move together until two meet up at one place
            while ptr1 != ptr2:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            return ptr2
    return 0
        
def get_length_cycle(head):
    count = 1
    curr = head.next
    # At the meet up point, we iterate again and count the loop
    while curr != head:
        curr = curr.next
        count += 1
    return count

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

main()