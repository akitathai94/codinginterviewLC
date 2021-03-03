# Given a singly linked-list, swap every two nodes of it. 
# Input : 2 -> 3 -> 4 -> 5 
# Output: 3 -> 2 -> 5 -> 4


class Node(): 
    def __init__(self, value, next = None):
        self.value = value 
        self.next = None


def print_function(head):
    temp = head
    while temp is not None:
        print(temp.value, end=" ")
        temp = temp.next
    print()
    
def swapNode(head):
    """ This function will swap every two Nodes. if uneven linkedlist the last node will stay the same"""
    curr = head
    count = 0
    while curr is not None:
        # write code here
        if (count == 0):
            prev = curr
        if (count == 1):
            # swap value prev and temp and reset count
            temp = prev.value
            prev.value = curr.value
            curr.value = temp
            count = -1
        count += 1
        curr = curr.next
    return head

# Testing
head = Node(2)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = Node(5)
head.next.next.next.next = Node(6)

print_function(head)
res = swapNode(head)
print_function(res)