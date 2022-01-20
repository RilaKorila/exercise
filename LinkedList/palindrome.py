# a Palindrome means 回文 in Japanese
# a word, phrase, or sequence that reads the same backwards as the forwards.

class ListNode(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
    # array solution: time O(n), space O(n)
    # def idPalindrome(self, head: ListNode) -> bool:
    #     nums = []

    #     while head:
    #         nums.append(head.val)
    #         head = head.next
        
    #     l, r = 0, len(nums)-1
    #     while(l <= r):
    #         if nums[l] != nums[r]:
    #             return False
    #         l += 1
    #         r -= 1

    #     return True

    # Linked List solution: time O(n), space O(1)