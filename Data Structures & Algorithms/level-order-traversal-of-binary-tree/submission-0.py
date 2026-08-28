# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        curr_node = root
        queue = collections.deque()
        res = []

        queue.append(curr_node)

        while len(queue) > 0:

            level = []
            qlen = len(queue)

            for i in range(qlen):

                curr_node = queue.popleft()
                
                if curr_node:
                    level.append(curr_node.val)
                    queue.append(curr_node.left)
                    queue.append(curr_node.right)

            if level:
                res.append(level)

        return res