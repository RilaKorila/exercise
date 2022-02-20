class Solution:
    def minCost(self, costs: List[List[int]])-> int:
        # cost[i][j]: i is house, j is color
        # dp = [[0, 0, 0] for i in range(len(costs))]
        
        # (house, color)
        # for i in range(2, 0, -1):
        #     for j in range(3):
        #         if not dp[i][j]:
        #             dp[i][j] = costs[i][j] + dp[i-1][j] + dp[i-2][j]
        
        # my code
        # for i in range(len(costs)):
        #     if i > 0:
        #         for j in range(3):
        #             dp = costs[i][j] + min(dp[i-1][j-1], dp[i-2][j-2])
                
        #     else:
        #         dp = costs[i][0]
        # return min(dp[-1])
        
        dp = [0,0,0]
        
        for i in range(len(costs)):
            dp0 = costs[i][0] + min(dp[1], dp[2])
            dp1 = costs[i][1] + min(dp[0], dp[2])
            dp2 = costs[i][2] + min(dp[1], dp[0])
            
            dp = [dp0, dp1, dp2]
        
        return min(dp)