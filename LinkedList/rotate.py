# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = ListNode()
        l.next = head
        
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        if length == 0:
            return None
        
        k = k%length
        
        if k==0:
            return head
        
        r = head
        while k>1:
            if not r :
                r = head
            r = r.next
            k-=1

        while r.next:
            r = r.next
            l = l.next
        
        r.next = head
        res = l.next
        l.next = None
        
        return res
    
        
        
        