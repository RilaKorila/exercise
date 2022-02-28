class Solution:
    # brute force -> Exceed Time
    def maxArea(self, height: List[int]) -> int:
        l = 0
        res = 0
        
        for l in range(len(height)-1):
            for r in range(l, len(height)):        
                res = max(res, min(height[l], height[r])*(r-l))
        
        return res
    
    def maxArea2(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        res = 0
        
        while l < r:
            res = max(res, min(height[l], height[r])*(r-l))
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
        