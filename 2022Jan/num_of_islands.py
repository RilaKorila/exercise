class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                # four directions: [right, left, above, below]
                directions = [[1,0], [-1,0], [0,1], [0,-1]]

                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    # inside of range?
                    if (r in range(rows)) and \
                    # inside of range?
                    (c in range(cols)) and \
                    # is islands?
                    grid[r][c] == "1" and \
                    # already checked?
                    (r, c) not in visit: 
                        q.append((r, c))
                        visit.add((r, c))
                

        for r in range(rows):
            for c in range(cols):
                # if we visited 0, we do nothing
                # if we visited 1, we start traversaling
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    # after calling bfs function, visit List is updated
                    islands += 1
        return islands