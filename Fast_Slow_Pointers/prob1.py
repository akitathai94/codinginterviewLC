"""
Given the head of a Singly LinkedList, 
write a function to determine if the LinkedList has a cycle in it or not.
"""
"""
Given the head of a LinkedList with a cycle, find the length of the cycle. 
"""
# Samples
# 1 --> 2 --> 3 --> 4 --> 5 --> 6 --> None return True

class Node:
    def __init__(self, value, next= None):
        self.value = value
        self.next = next

def has_cycle(head):
    # Initialize slo, fas pointer to head 
    slo, fas = head, head
    # while condition: if fas != None or fas.next != None
    while fas != None and fas.next != None:
    # else slo jump 1, fas jump 2 
        slo = slo.next
        fas = fas.next.next
        if fas == slo:
            return True
    # check if fas.next == slo return True
    # outside the loop return False
    return False
def find_cycle_length(head):
    slo, fas = head, head
    while fas != None and fas.next != None:
        slo = slo.next
        fas = fas.next.next
        if fas == slo:
            return get_cycle_length(slo)
    return 0
def get_cycle_length(slow):
    curr = slow.next
    len = 1
    while curr != slow:
        len += 1
        curr = curr.next
    return len
def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  print("LinkedList has cycle: " + str(has_cycle(head)))
  head.next.next.next.next.next.next = head.next.next
  print("LinkedList has cycle: " + str(has_cycle(head)))
  print("LinkedList has cycle length: ", find_cycle_length(head))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList has cycle: " + str(has_cycle(head)))
  print("LinkedList has cycle length: ", find_cycle_length(head))

main()