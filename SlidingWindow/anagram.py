class Solution:
    def findAnagrams(self, s:str, p:str)-> List[int]:
        if len(p) > len(s):
            return []
        
        pCount, sCount = {}, {}
        for i in range(len(p)):
            # pCount.get(s[i], 0): if s[i] is not included in pCount.keys, it returns default value(0) 
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
        
        res = [0] if sCount == pCount else []
        l = 0
        
        for r in range(len(p), len(s))        :
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1
            
            if sCount[s[l]] == 0:
                # we compare with whole dictionary
                sCount.pop(s[l])
            l+=1
            if sCount == pCount:
                res.append(l)
        
        return res
    
    
    #     l, r = 0, len(p)
    #     s_count = {}
    #     p_count = {}
        
    #     for c in p:
    #         if not c in p_count.keys():
    #             p_count[c] = 0
    #         p_count[c] += 1
        
    #     sub = s[l:r]
    #     for c in sub:
    #         if not c in s_count.keys():
    #             s_count[c] = 0
    #         s_count[c] += 1
        
    #     res = []
    #     while r < len(p):
    #         if not s[r] in p:
    #             l = r+1
    #             r = l + len(p)
    #         sub = s[l:r]
    #         s_count[s[r]] += 1 
    #         if s_count == p_count:
    #             res.append(l)
    #         s_count[s[l]] -= 1 
    #         r+=1
    #         l+=1
        
    #     return res
        