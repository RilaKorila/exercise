class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2
        
        for i in range(len(nums)-1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t+nums[i]) == target:
                    return True
                # the sum of each value in dp + each value in nums
                nextDP.add(t+nums[i])
                # add original value in dp to nextDP
                nextDP.add(t)
            dp = nextDP
        return True if target in dp else False
                