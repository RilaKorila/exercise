# This problem is quite famous.
# Stack: First In Last Out
# o: [({})]
# x: [(])
# At first, we see open parenthesis until we see closed parenthesis
from asyncio import format_helpers


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(",
                       "]": "[",
                       "}": "{"}
        
        # check every character of input string
        for c in s:
            # if c is close parenthesis
            if c in closeToOpen:
                # we would like to make sure
                # stack is not empty & the value is matching open parenthesis
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            # if c is open parenthesis
            else:
                # if we get open parenthisis
                stack.append(c)
                
        # empty stack means all open parenthesis had its close parenthesis validly
        return True if not stack else False
        