class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        # the code which I wrote at first
        # l, r = 0, num//2
        
        # # O(log n)
        # while l <= r:
        #     m = (l+r) // 2
        #     val = m+1
            
        #     if num == val**2:
        #         return True
        #     elif num > val**2:
        #         l = m+1
        #     else:
        #         r = m-1
                
        # return False
        
        
        l, r = 1, num
        
        while l <= r:
            m = (l+r) // 2
            
            if num == m**2:
                return True
            elif num > m**2:
                l = m+1
            else:
                r = m-1
        return False