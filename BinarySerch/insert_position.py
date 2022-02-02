class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums)-1
        
        # while l<=r:
        #     m = (l+r)//2
        #     if target <= nums[m]:
        #         r = m-1
        #         if nums[m-1] < target < nums[m]:
        #             return m
        #     elif target >= nums[m]:
        #         l = m+1
        #         if nums[m] < target < nums[m+1]:
        #             return m

        # At first, we have to check whether target is equal to values in middle
        # while l<=r:
        #     m = (l+r)//2  
        #     if target == nums[m]:
        #         return m
            
        #     # if nums[m] is not equal to target
        #     if target > nums[m]:
        #         l = m+1
        #         if m+1 == len(nums):
        #             return len(nums)
                    
        #         elif nums[m+1] > target:
        #             return m
        #     else:
        #         r = m-1
        #         if target > nums[m-1]:
        #             return m
        
        
        # Neetcode
        while l<=r:
            m = (l+r)//2  
            if target == nums[m]:
                return m
            
            # if nums[m] is not equal to target
            if target > nums[m]:
                l = m+1
            elif target < nums[m]:
                r = m-1
        return l
                