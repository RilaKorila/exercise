#  [WIP] 
class Solution:
    def pacificAtlantic(self, height: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or r < 0 or c < 0 or r==ROWS or c==COLS or heights[r][c] < preHeight):
                return 
            
            visit.add((r,c))
            # Check all neighbors
            dfs(r+, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        for c in range(COLS):
            # 一番上の行をみる: 
            dfs(0, c, pac, heights[0][c])
            # 一番下の行をみる: 
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, alt, heights[r][COLS-1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in alt:
                    res.append([r,c])
        
        return res