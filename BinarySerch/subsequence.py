class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        # n: how long it takes to search sub sequence, k: length of removable list   
        # brute force: O(nk)
        # binary search: 0(n log(k))
        
        def isSubsequence(s, subseq):
            # i1: pointer for s
            # i2: pointer for subseq
            i1, i2 = 0, 0
            
            while i1 < len(s) and i2 < len(subseq):
                # 1. if value in i1 is included removed list, we can skip it
                # 2. if the character in s is different from character in subsequence, 
                # we have to check next character is s
                if i1 in removed or s[i1] != subseq[i2]:
                    # only i1 will be shifted to next position
                    i1 += 1
                    # continue next iteration loop
                    continue
                # if we find part of subseq, both pointer will be shifted
                i1 += 1
                i2 += 1
            
            return i2 == len(subseq)
            # ↑ in the situation, i2 can reach at the end of the subsequence
        
        res = 0 
        # we will do bin search on removable
        l, r = 0, len(removable)-1
        
        while l<=r:
            m = (l+r)//2
            
            # the position we already removed from 
            removed = set(removable[:m+1])
            if isSubsequence(s, p):
                # we have to return the number of removable characters, not index
                res = max(res, m+1)
                l = m+1
            else:
                r = m-1
        return res

# ---
# Why binary search is efficient in this problem?