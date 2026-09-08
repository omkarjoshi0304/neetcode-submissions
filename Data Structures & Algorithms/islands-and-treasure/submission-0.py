class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row , col = len(grid) , len(grid[0])
        queue = deque()
        visit = set()

        for r in range(row):
            for c in range (col):
                if grid[r][c] == 0:
                    queue.append([r , c])
                    visit.add((r , c))
        def addroom(r , c):
            if (r < 0 or r >= row or c < 0 or c >= col or (r, c) in visit or grid[r][c] == -1):
                return
            visit.add((r ,c))
            queue.append([r , c])
        dist = 0
        while queue:
            for i in range(len(queue)):
                r , c = queue.popleft()
                grid[r][c] = dist
                addroom(r + 1 , c)
                addroom(r - 1 , c)
                addroom(r , c + 1)
                addroom(r , c - 1)
            dist += 1