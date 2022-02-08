class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # --- Condition to solve this problems ------
        # 1. only add open parenthesis if open < n
        # 2. only add a closing parenthesis if closed < open 
        # valid IIF open == closed == n
        
        stack = []
        res = []
        
        def backtrack(openN: int, closedN:int) -> None:
            # base case
            if openN == closedN == n:
                # join every characters in stack
                res.append("".join(stack))
                return res
            
            if openN < n:
                # we can add open parenthesis
                stack.append("(")            
                backtrack(openN+1, closedN)
                # after return backtrack function, we have to update(=Clean) stack
                stack.pop()
            
            if closedN < openN:
                # we can add closed parenthesis                
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()
        
        backtrack(0,0)
        return res