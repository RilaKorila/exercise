# days: the days of the year which you travel
# costs: each cost of [a 1-day pass, a 7-days pass, a 30-day pass]
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # cache to stop doing the same things
        dp = {}
        
        def dfs(i):
            # i: the day when start　travel
            if i == len(days):
                return 0
            
            if i in dp:
                return dp[i]
            
            dp[i] = float("inf")
            for d, c in zip([1, 7, 30], costs):
                j = i
                # if j is inside of range, and days we can travel for
                while j < len(days) and days[j] < days[i]+d:
                    j += 1
                # i+d: current day + days we buy a passport for
                # -> j: what is the next day that we'll actually need to purchase a travel pass on
                dp[i] = min(dp[i], c+dfs(j))
            
            return dp[i]
        
        # 0 is index of days array   
        return dfs(0)
    
    
    def dp_sol(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        for i in range(len(days)-1, -1, -1):
            dp[i] = float("inf")
            
            for d, c in zip([1, 7, 30], costs):
                j = i
                while j<len(days) and days[j]<days[i]+d:
                    j += 1
                
                # dp.get(key, returnVal): 辞書を使用し、keyがなければreturnValを返す
                # get以外で辞書のvalueにアクセスしたときにもErrorが出ないようにする
                dp[i] = min(dp[i], c+dp.get(j, 0))
        
        return dp[0]
        