# we can climb 1 or 2 steps each time
class Solution:
    def climbStairs(self, n: int) -> int:
        # DP: store memory, and skip the same execution
        one, two = 1, 0
        
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        
        return one