class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        # current partition
        part = []
        
        def dfs(i):
            # base case
            if i >= len(s):
                res.append(part[:])
                return
            
            # generate every single possible substring and check whether it is palindrome
            for j in range(i, len(s)):
                # substring:s[i:j+1]
                if self.isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    # すでにチェックしたみた枝まで戻る
                    part.pop()
        
        dfs(0)
        return res
                
                
    
    def isPalindrome(self, s: str, l:int, r:int) -> bool:
            
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True
                