class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        numDic = {'M': 1000, 'D': 500, 'C': 100, 'L':50, 'X':10, 'V':5, 'I':1}

        
        for i, c in enumerate(s):
            res += numDic.get(c)
        
        if "IV" in s:
            res -= 6
            res += 4
        if "IX" in s:
            res -= 11
            res+=9
        if "XL" in s:
            res -= 60
            res+=40
        if "XC" in s:
            res -= 110
            res+=90
        if "CD" in s:
            res -= 600
            res += 400
        if "CM" in s:
            res -= 1100
            res += 900
        
            
        
            # if c=='I':
            #     if s[i+1]=='x':
            #         res += 4
            #     elif s[i+1]=='V':
            #         res += 9
            # elif c=='X':
            #     if s[i+1]=='L':
            #         res += 40
            #     elif s[i+1]=='C':
            #         res += 90
            # elif c=='C':
            #     if s[i+1]=='D':
            #         res += 400
            #     elif s[i+1]=='M':
            #         res += 900
                    
            # else:
            #     res += numDic.get(c)
            
        return res
        