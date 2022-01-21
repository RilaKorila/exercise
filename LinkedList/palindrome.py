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

    # 2 Pointer solution: time O(n), space O(1)
    # Fast Pointer 
    # when Fast Pointer reach at the end of list, slow pointer reached at middle of the list
    class Solution:
        def isPalindrome(self, head: ListNode) -> Npnel:
            fast = head
            slow = head

            # find middle (slow)
            while fast and fast.next:
                # fast pointer is twice faster than slow pointer
                fast = fast.next.next
                slow = slow.next

            # reverse second half
            prev = None
            # until reach at the end
            while slow:
                temp = slow.next
                slow.next = prev
                prev = slow
                slow = temp
            
            # check palindrom
            left , right = head, prev
            while right:
                if left.val != right.val:
                    return False
                
                left = left.next
                right = right.next

            return True

                