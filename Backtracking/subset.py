class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        # global access
        subset = []
        
        # i: index of the value we decide whether we should add it or not
        # dfs: nums[i]を含むsubsetと含まないsubsetをresにappendする関数
        def dfs(i: int) -> None:
            if i >= len(nums):
                # append the copy of subset
                res.append(subset[:])
                return 
            
            # We have to think whether nums[i] should use subset element or not
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1) # given different subset
            
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i+1) # given empty subset
        
        dfs(0)
        
        return res
    
    # those who watched the video was wrote this code as comment
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        
        res=[[]]
        for i in nums:
            new=[]
            for t in res:
                new.append(t)
                new.append(t+[i])
            res=new
                                                
        return res
                
    
    # my first code
    # generate ALL subset, cannot remove duplicate subsets
    # def subsets(self, nums: List[int]) -> List[List[int]]:
        
    #     result = [[]]
        
    #     for i in range(len(nums)):
    #         if len(nums) == i:
    #             return [nums[:]] if 
        
            
    #         n = nums.pop(0)
    #         subsets = self.subsets(nums)
            
    #         for subset in subsets:
    #             subset.append(n)
    #             if subset not in result:
    #                 result.append(subset)
            
    #         nums.append(n)
        
    #     return result