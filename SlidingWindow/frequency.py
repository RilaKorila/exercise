class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # O(log n)
        nums.sort()
        
        l, r = 0, 0
        res, total = 0, 0
        
        # O(n)
        while r < len(nums):
            total += nums[r]
            
            # r-l+1: length of window
            while nums[r]*(r-l+1) > total + k:
                # shrink the window
                total -= nums[l]
                l += 1
            res = max(res, r-l+1)
            r += 1
        return res