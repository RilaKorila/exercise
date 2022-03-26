# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = l1
        kurai = 1
        res = 0
        while cur:
            res += cur.val * kurai
            kurai *= 10
            cur = cur.next
        
        
        cur = l2
        kurai = 1
        res2 = 0
        while cur:
            res2 += cur.val * kurai
            kurai *= 10
            cur = cur.next
        res_str = str(res+res2)
        
        
        dummy = ListNode()
        dummy.next = ListNode(res_str[-1])
        cur =  dummy.next
        for i in range(len(res_str)-2, -1, -1):
            cur.next = ListNode(res_str[i])
            cur = cur.next
        
        return dummy.next