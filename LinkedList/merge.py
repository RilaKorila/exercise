# merge two lists
# to avoid edge case, we will make dummy node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        # both of nodes from list1 and list2 are not none
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            # update tail pointer
            tail = tail.next

        # in the case that one of them is empty
        if l1:
            tail.next = l1
        else:
            tail.next = n2
        
        
        return dummy.next