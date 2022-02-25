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
                