class Solution:
    def simplifyPath(self, path: str) -> str:
        # .. refer to the directory up a level
        # but, if we are in already root dir, we will stay there
        # stack: First In Last Out (.. is equal to stack calling pop())
        
        stack = []
        cur = ""
        
        for c in path + "/":
            if c == "/":
                if cur == "..":
                    # if we are in root directory, we cannot pop
                    if stack:
                        stack.pop()
                elif cur != "" and cur != ".":
                    stack.append(cur)
                # reset current directory
                cur = ""
            else:
                cur += c
        
        # join every string in a stack
        return "/" + "/".join(stack)