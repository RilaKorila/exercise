# linear search: O(n)
# binary search: O(log n)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # leftBias[bool] : if false, result is rightBiased = search minimum index
        def binSearch(self, nums, target, leftBias):
            l, r = 0, len(nums)-1
            
            while l <= r:
                # m: middle index of bin search
                m = (l+r) // 2
                if target > nums[m]:
                    l = m+1
                elif target < nums[m]:
                    r = m-1
                else:
                    i = m
                    
                    # even if we find target, we continue to search min index
                    if leftBias:
                        r = m-1
                    # we search max index
                    else: # rightBiased
                        l = m+1
            
            return i
        
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        
        return [left, right]
        
            