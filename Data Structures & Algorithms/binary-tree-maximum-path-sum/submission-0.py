# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = [root.val]

        def dfs (root):

            if not root:
                return 0

            
            root.left = dfs(root.left)
            root.right = dfs(root.right)

            leftmax = max(root.left , 0)
            rightmax = max(root.right, 0)

            res[0] = max(res[0] , root.val + leftmax + rightmax)

            return root.val + max(leftmax , rightmax)

        dfs(root)
        return res[0]        