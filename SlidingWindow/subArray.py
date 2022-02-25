class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        res = len(nums)+1
        while r < len(nums):
            if sum(nums[l:r+1]) >= target:
                res = min(res, r+1-l)
                l += 1

            else: # sumSub < target
                # まだ足せる
                r += 1

        return res if res != len(nums)+1 else 0
    
    def NeetCode(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        res = float("inf")
        
        for r in range(len(nums)):
            total += nums[r]
            
            # if condition(total >= target) continues, we continue to increase left pointer 
            while total >= target:
                # res is size of the window
                res = min(res, r-l+1)
                # update the window
                total -= nums[l]
                l += 1
                
        
        
        return 0 if res == float("inf") else res
                