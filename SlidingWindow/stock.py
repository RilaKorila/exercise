# maximize your profit by choosing a single day to buy and choosing a different day in the future to sell
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # left = buy, right = sell
        maxP = 0
        
        while r < len(prices):
            # profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            
            else:
                # if prices[l] >= prices[r], 
                # we should buy the stock on the "right" day since prices[r] is lower price than prices[l]
                l = r
                # l+=1
            r += 1

        return maxP