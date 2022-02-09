# brute force = Backtracking
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        # we do not want to visit the same position
        # nodes in current path
        path = set()
        
        # r, c: position
        # i: index for word
        def dfs(r, c, i):
            # check whether CURRENT position is True or False
            # if we reach at the end of the word
            if i == len(word):
                return True
            if r<0 or c<0 or r>=ROWS or c>=COLS or word[i]!=board[r][c] or (r,c) in path:
                return False
            
            # we want to go to check next position
            path.add((r, c))
            # if any of 4 direction is valid, we return true
            res = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1))

            # unless we go through the path, we continue to add nodes to the path,
            # but once we realize the path is invalid, we have to search new path and at that time we want to use brand new path()
            path.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        # if all path is not True
        return False
    
    # O(n * m * dfs) 
    # dfs = 4 * len(word) 
    # アルゴリズム全体では、O(n^2 * m)
            
        