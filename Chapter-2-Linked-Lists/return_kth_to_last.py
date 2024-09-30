'''
2.2
Return Kth to Last

Implement an algorithm to find the kth to last element of a singly linked list.
'''

# Only for generating LinkedList for testing
import random

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def return_kth_to_last(head: ListNode, k: int) -> int:
    buffer = head
    trail = head

    for i in range(k):
        if buffer is None:
            return None
        buffer = buffer.next
    
    while buffer is not None:
        trail = trail.next
        buffer = buffer.next
    
    return trail.val

def generate_sample_linked_list(size: int) -> ListNode:
    if size <= 0:
        return None
    head = ListNode(random.randint(0, 99))
    current = head
    for _ in range(size - 1):
        current.next = ListNode(random.randint(0, 99))
        current = current.next
    return head


if __name__ == "__main__":
    # Alter to test with larger linked_lists
    linked_list = generate_sample_linked_list(10)
    # Alter to change k
    k = 2
    ans = return_kth_to_last(linked_list, k)
    head = linked_list
    while head is not None:
        print(head.val)
        head = head.next
    print(f"The kth-last element ({k}) in linked_list is: {ans}")
