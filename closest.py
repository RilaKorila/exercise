class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr)-1
        
        while l<=r:
            m = (l+r)//2
            
            if x < arr[m]:
                r = m-1
            elif arr[m] < x:
                l = m+1
            
        