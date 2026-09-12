class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {i: [] for i in range(len(points))}

        for i in range(len(points)):
            x1 , y1 = points[i]
            for j in range( i + 1 , len(points)):
                x2  , y2 = points[j]
                dist = abs(x1 - x2) +  abs(y1 - y2)
                adj[i].append([dist , j])
                adj[j].append([dist, i])
        
        res = 0
        minHeap =[[0 , 0]]
        visit =set()
        while len(visit) < len(points) :
            cost, i = heapq.heappop(minHeap)

            if i in visit :
                continue
            
            res += cost
            visit.add(i)
            for neicost , nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minHeap ,[neicost , nei])
        return res
