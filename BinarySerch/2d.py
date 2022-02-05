class Solution:
    def mySearchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row which may include target by forcusing on the head of each row
        up, down = 0, len(matrix[0])-1
        
        cur = 0
        while up <= down:
            mid = (up+down)//2
            
            # if matrix[up][0] <= target <= matrix[mid][0]:
            #     down = mid-1
            # elif matrix[mid][0] < target <= matrix[down][0]:
            #     up = mid+1
            # else:
            #     target_row = matrix[down][0]
            if target <= matrix[mid][0]:
                cur = mid
                down = mid-1
            else:
                up = mid+1       
        
        cur = mid
        print(cur)
        l, r = 0, len(matrix[cur])
        # search the row which may include target
        while l < r:
            m = (l+r)//2
            print(l, r)
            
            if matrix[cur][m] == target:
                return True
            
            elif matrix[cur][m] > target:
                r = m-1
            else:
                l = m+1
        
        return False
            
    # O(log m * log n)
    def mySearchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row which may include target by forcusing on the head of each row
        ROWS, COLS = len(matrix), len(matrix[0])
        
        top, bot = 0, ROWS-1
        while top <= bot:
            row = (top+bot)//2
            
            if target > matrix[row][-1]:
                top = row+1
            elif target < matrix[row][0]:
                bot = row-1
            # target is too big, or too small
            else:
                break
        
        # "top <= bot" means we cannot find target in first search
        if not (top <= bot):
            return False
        
        row = (top+bot) // 2
        l, r = 0, COLS-1
        while l <= r:
            m = (l+r)//2
            if target > matrix[row][m]:
                l = m+1
            elif target < matrix[row][m]:
                r = m-1
            else:
                return True
        return False
                
                
        