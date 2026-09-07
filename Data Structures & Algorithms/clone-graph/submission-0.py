"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
            
        oldToNew = {} # Map: Original Node -> Cloned Node
        
        def dfs(node):
            # 1. Base Case: We already cloned this node. Return the clone!
            if node in oldToNew:
                return oldToNew[node]
                
            # 2. CHOOSE: Create the clone and immediately map it
            copy = Node(node.val)
            oldToNew[node] = copy
            
            # 3. EXPLORE: Recursively clone all neighbors and wire them up
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
                
            # 4. Return the fully wired cloned node
            return copy
            
        return dfs(node)