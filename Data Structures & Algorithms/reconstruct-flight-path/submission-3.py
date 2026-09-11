import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        
        tickets.sort(reverse=True)
        for src, dst in tickets:
            adj[src].append(dst)
            
        res = []
        
        def dfs(airport):

            while adj[airport]:

                next_dest = adj[airport].pop()
                dfs(next_dest)
                
            res.append(airport)
            
        dfs("JFK")
        
        return res[::-1]