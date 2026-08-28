# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        q = collections.deque()
        q.append(root)
        res = []

        while len(q) > 0:

            right = None
            lenq = len(q)

            for i in range (lenq):

                node = q.popleft()

                if node:
                    right = node
                    q.append(node.left)
                    q.append(node.right)
                
            if right:
                res.append(right.val)
        return res
