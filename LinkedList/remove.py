# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head; ListNode, val: int) -> ListNode:
        dummy = ListNode(next=head)
        prev, cur = dummy, head

        # while current Node is not None
        while cur:
            nxt = cur.next

            if cur.val == val:
                # we can delete current Node
                
                # current Node is skipped
                prev.next = nxt
                # we don't have to update prev pointer, 
                # because we deleted current pointer and now prev pointer is before cur.next Node
            else:
                # we do not delete node
                prev = cur
            
            cur = nxt
        
        return dummy.next
