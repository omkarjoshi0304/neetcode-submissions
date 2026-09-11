import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        
        # 1. Sort in REVERSE alphabetical order.
        # This puts the alphabetically smallest destinations at the END of the list,
        # meaning we can use .pop() to grab them in O(1) constant time!
        tickets.sort(reverse=True)
        for src, dst in tickets:
            adj[src].append(dst)
            
        res = []
        
        def dfs(airport):
            # 2. Keep flying as long as we have tickets out of this airport
            while adj[airport]:
                # Grab the next destination and immediately fly there
                next_dest = adj[airport].pop()
                dfs(next_dest)
                
            # 3. We hit a dead end! No more outgoing flights.
            # Because a valid path is guaranteed, this MUST be the end of the line.
            res.append(airport)
            
        dfs("JFK")
        
        # 4. Because we wrote the final destinations first, reverse the list
        return res[::-1]