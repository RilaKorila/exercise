# return binary string which is not included in given array
# if there multiple answers, return any of them

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        strSet = {s for s in nums} 

        # solve recursively
        def backtrack(i, cur):
            # base case
            if i == len(nums):
                # check whether res char set is included in strSet
                res = "".join(cur)
                # if we find res in strSet, it is not answer
                return None if res in strSet else res
            
            # shift next position
            res = backtrack(i+1, cur)
            # if res is not None
            if res:
                # backtrack return either None or res
                return res
            # we don't have to generate extra string
            
            # default value is all 0
            cur[i] = "1"
            res = backtrack(i+1, cur)
            if res:
                return res
        
        # guarantee backtrack returns valid answer
        return backtrack(0, ["0" for s in nums])