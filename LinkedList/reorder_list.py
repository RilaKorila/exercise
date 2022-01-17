# we would like to solve this problem with O(n) time and O(1) space
# 1. take second half of List 
# 2. change direction of second List
# 3. merge two Lists
# last node of new List point out NULL


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        #  slow: a head of List, fast: next of a head

        # find middle
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two half Lists
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1 # first.next
            first, second  = tmp1, tmp2
