class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        Row , Col = len(grid) , len(grid[0])
        q = deque()
        time ,fresh = 0 , 0
        for r in range(Row):
            for c in range(Col):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r , c])

        dir = [[0 , 1], [0 , -1], [1 ,0] ,[- 1 , 0]]
        while q and fresh > 0:
            for i in range(len(q)):

                r , c = q.popleft()
                for dr , dc in dir:
                    row , col = r + dr , c + dc
                    

                    if (row < 0 or col < 0 or row >= Row or col >= Col  or grid[row][col] != 1):
                        continue
                    
                    grid[row][col] = 2
                    q.append([row , col])
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1