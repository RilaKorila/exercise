# we solve this problem with O(log n) runtime complexity
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        def isInLeftPotion(m):
            return nums[0] <= nums[m] 
        
        while l<=r:
            m = (l+r)//2
            
            if isInLeftPotion(m):
                if nums[m] < target:
                    # target is in difinitely right side
                    l = m+1
                elif nums[m] > target:
                    # both side is possible
                    if nums[l] < target:
                        # target is between l and m
                        r = m-1
                    elif nums[l] > target:
                        l = m+1
                    else:
                        return l
                else:
                    return m
               
            # m is in right potion
            else:
                if target < nums[m]:
                    # target is definitely in left side
                    r = m-1
                    
                elif nums[m] < target:
                    # both side is possible
                    if target < nums[r]:
                        # target is between m and r:
                        l = m+1
                    elif target > nums[r]:
                        r = m-1
                    else:
                        return r

                else:
                    return m
                    
                    
        return -1
    # ----- can write by myself ^^ -----------
    
   
    
        