from tkinter.tix import ROW


class SubSum:
    # Brute Force
    def bf_sum(self, nums: List[int], cur: int, limit: int)-> int:
        
        # cur: index
        # limit: max of sum
        if cur >= len(nums) or limit <= 0:
            return 0
        
        else:
            tmp_not_choice = self.bf_sum(nums, cir+1, limit)
            if nums[cur] > limit:
                return tmp_not_choice
            else:
                tmp_choice = self.bf_sum(nums, cur+1, limit-nums[cur]) + nums[cur]
                return max(tmp_choice, tmp_not_choice)
        
    def dp_sum(self, nums: List[int], limit: int)-> int:
        COLS, ROWS = limit+1, len(nums)
        dp_table = [[0 for i in range(COLS)] for j in range(ROWS)]
        
        # first card
        for j in range(limit+1):
            # value of first cards is smaller than index
            if nums[0] < j:
                dp_table[0][j] = nums[0]
            # dp_table is initialized by 0, so we don't have to fill other cell
        
        # rest cards
        for i in range(1, ROWS):
            for j in range(COLS):
                # check the above table
                tmp_not_choice = dp_table[i-1][j]
                # if the value of card i is more than cost, 
                # we do not add the value (= add the same value as the above cell)
                if nums[i] > j:
                    dp_table[i][j] = dp_table[i-1][j]
                else:
                    dp_table[i][j] = max(dp_table[i-1][j], dp_table[i-1][j-nums[i]]+nums[i])
                
        return dp_table[-1][-1]
                    
                
                
            
        
                
        
                