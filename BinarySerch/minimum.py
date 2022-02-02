class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find decreasing order: the position is the end of original list
        # we want to know middle value is in right sorted potion or left sorted position
        res = nums[0]
        l,r = 0, len(nums)-1
        
        # keep running binary search while left pointer is small equal to right pointer
        while l <= r:
            # nums[l] is smallest in left sorted potion
            # nums[r] is smallest in right sorted potion
            # even if left and right is in same position, <= is not necessary 
            # because we will check nums[m] vs res later
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l+r) // 2
            # check whether middle value is smallest or not
            res = min(res, nums[m])
            
            # if left potion is increasing order, we should search right potion
            if nums[m] >= nums[l]:
                l = m+1
            # if left potion is decrasing order, we should search left potion
            else:
                r = m-1
        return res
                
        