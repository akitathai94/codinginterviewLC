# Given a head of a LinkList and two positions 'p' and 'q', reverse the Linklist from pos p to q
# Example: 1 -> 2 -> 3 -> 4 -> 5 -> null
# p = 2, q = 4
# 1 -> 4 -> 3 -> 2 -> 5 -> null

# define Node
class Node():
    def __init__(self, value, next = None):
        self.value = value
        self.next = None

    def print_function(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()
    
def reverse_sub_List(head, p, q):
    # write your code here
    # We only care about 3 parts: first part is before p, between p and q, and after q
    if p == q:
        return head
    curr = head
    previous = None
    i = 0
    while curr is not None and i < p -1:
        previous = curr
        curr = curr.next
        i += 1

    last_node_first_part = previous
    # This node later will become last node second part
    last_node_second_part =curr 
    # First get the node before p
    i = 0
    while curr is not None and i < q - p + 1:
        next = curr.next
        curr.next = previous
        previous = curr
        curr = next
        i += 1
    
    # Check if last_node_first_part is null (if the node we start to swap is end of linklist)
    if last_node_first_part is not None:
        last_node_first_part.next = previous
    else:
        head = previous

    # assign last_node_second_part.next to curr for last node
    last_node_second_part.next = curr
    return head

# Testing         
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Node of original Linklist are: ",end=" ")
head.print_function()

res = reverse_sub_List(head, 2, 4)

print("Node of reverse LInklist are: ", end=" ")
res.print_function()

