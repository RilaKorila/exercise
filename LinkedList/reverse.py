# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         while True:
#             # no.1
#             tmp1 = head 
#             # no.2
#             tmp2 = head.next
            
#             head.next = tmp2.next
#             head = tmp2
            
            
#             if head.next == None:
#                 break
        
#         res = []
#         while True:
#             if head.next and head:
#                 print(head.val)
#                 res.append(head.val)
#             if not head.next:
#                 break
        
#         return head

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur =  None, head

        # Time: O(n), Memory: O(1)
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

        # recursive:  Time: O(n), Memory: O(n)
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead