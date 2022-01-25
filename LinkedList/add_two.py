# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        carry = 0
        # while l1 pr l2 is not none
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = v2.val if l2 else 0

            # new digit
            cal = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = List(mode)
