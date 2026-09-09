class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 1. Edge Case: A valid tree MUST have exactly n - 1 edges
        if len(edges) != n - 1:
            return False
            
        # 2. Build the Adjacency List for an UNDIRECTED graph
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1) # Must append to both sides!
            
        visit = set()
        
        def dfs(node, prev):
            # 3. Genuine Cycle detected!
            if node in visit:
                return False
                
            visit.add(node)
            
            # 4. Explore all neighbors
            for nei in adj[node]:
                # 5. Skip the node we literally just came from
                if nei == prev:
                    continue
                # If any branch finds a cycle, bubble up the failure
                if not dfs(nei, node):
                    return False
                    
            return True
            
        # 6. Start DFS from node 0. It has no previous node, so pass -1
        if not dfs(0, -1):
            return False
            
        # 7. Check for floating islands (Disconnected graph)
        return len(visit) == n