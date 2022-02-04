# koko eats all bananas from all piles until the guardian comes back
# len(piles) < h: 
# if the number of piles is more than h, koko cannot eat all bananas even if she eats tons of bananas per hour

# 1. brute force: O(max(piles)・piles)
# we check k from 1 to max value in piles list

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canEatAllBananas(piles, k, h):
            time = 0
            for pile in piles:
                if pile%k == 0:
                    time += (pile // k)
                else:
                    time += (pile // k) + 1
                
                # math.ceil(pile/k)
            return time <= h
        
        
        l, r = 1, max(piles)
        
        k = -1
        while l<=r:
            m = (l+r)//2
            if canEatAllBananas(piles, m ,h):
                k = m
                r = m-1
            else:
                l = m+1
        
        return k        
        
# I wrote all code by myself ^^