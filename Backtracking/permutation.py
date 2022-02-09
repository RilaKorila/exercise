class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        # base case
        if len(nums) == 1:
            # if we get [1] as input, return [[1]]
            return [nums[:]]
            # return [nums.copy()]
        
        
        for i in range(len(nums)):
            # [1, 2, 3]の1: pop 0 index
            n = nums.pop(0)
            
            # recursive call
            perms = self.permute(nums)
            # ex) perms has [[2,3] [3,2]]
            # -> Next, we want to append 1 at the end of the each List
            # n is a value which poped 
            
            for perm in perms:
                perm.append(n)
            # add multiple elements to array (python function)
            result.extend(perms)
            nums.append(n)
        
        return result
        