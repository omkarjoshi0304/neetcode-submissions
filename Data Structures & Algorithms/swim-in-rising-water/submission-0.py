class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)

        minHeap = [[grid[0][0] , 0 , 0]]

        visit = set()
        dirs = [[0 , 1] , [0 , -1 ], [1 , 0] ,[-1 , 0]]
    
        while minHeap:
            t , r , c = heapq.heappop(minHeap)

            if r == N -1 and c == N - 1:
                return t

            for dr , dc in dirs:
                neir , neic = dr + r , dc + c
                if (neir < 0 or neic < 0 or neir == N or neic == N or (neir , neic) in visit ):
                    continue
                visit.add((neir , neic))
                heapq.heappush(minHeap ,[max(t , grid[neir][neic]), neir , neic])

