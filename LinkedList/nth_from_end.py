# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from re import L


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        cur = head
        while cur.next:
            length+=1
            cur = cur.next
        
        pre = ListNode()
        pre.next = head
        
        place = length-n
        cur = pre
        while place>0:
            place -= 1
            cur = cur.next

        cur.next = cur.next.next
        
        return pre.next
        
    # one path solution
    def TwoPointerSolution(self, head: Optional[ListNode], n:int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # move right pointer
        # distance btw left and right should be n
        while n>0 and right:
            right = right.next
            n -= 1
        
        # keeping the distance, move both pointer
        # until right pointer reach at the end of LinkedList
        while right:
            left = left.next
            right = right.next
        
        # delete node which left pointer is pointing
        left.next = left.next.next
        
        return dummy.next
