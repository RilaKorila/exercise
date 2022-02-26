class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s += s
        # alt1: alternating string starting with 0
        # alt2: alternating string starting with 1
        alt1, alt2 = "", ""
        
        for i in range(len(s)):
            alt1 += "0" if i%2 else "1"
            alt2 += "1" if i%2 else "0"
        
        res = len(s)
        diff1, diff2 = 0, 0
        l = 0
        # first half
        for r in range(n):
            if s[r] != alt1[r]:
                diff1 += 1
            if s[r] != alt2[r]:
                diff2 += 1
        
        # second half
        for r in range(n, len(s)):   
            if s[r] != alt1[r]:
                diff1 += 1
            if s[r] != alt2[r]:
                diff2 += 1
                
            if s[l] != alt1[l]:
                diff1 -= 1
            if s[l] != alt2[l]:
                diff2 -= 1
            l += 1
            
            res = min(res, diff1, diff2)
                
        return res