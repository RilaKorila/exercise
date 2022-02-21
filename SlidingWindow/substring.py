class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        l, r = 0,  1
        maxLen = 1
        sub = [s[l]]
        
        while r < len(s):
            if not s[r] in sub:
                sub.append(s[r])
                maxLen = max(maxLen, r-l+1)
            else:
                # reset substring
                l += 1
                sub = [s[l]]
                r = l
            r += 1
        
        return maxLen
    
    def faster(self, s:str) -> int:
        charSet = set()
        l, res = 0, 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            res = max(res, r-l+1)
        
        return res
            