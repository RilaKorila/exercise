# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

# Example 1: n=10
# 1から10までの数字の中に、targetがある
# 相手が　1から10の中から数字を1つ選ぶ → 6 (自分は知らない)

# guess(数字)　＝＞　大きい？小さい？

class Solution:
    def guessNumber(self, n: int) -> int:
        # guess(3) -> lower : 1
        
        l, r = 1, n
        
        while l <= r:
            m = (l+r)//2
            
            
            # m はtargetより大きい
            if guess(m) == -1:
                r = m-1
                
            # m は targetよりも小さい
            elif guess(m) == 1:
                l = m+1
            
            else:
                return m
            
        
                
                
                
            
        

        