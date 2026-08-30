# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map each value to its index in inorder for instant O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Keep a pointer to track the current root in the preorder array
        self.pre_idx = 0 
        
        # Helper function that only uses boundary indices, no array slicing!
        def build(left, right):
            # Base Case: If boundaries cross, there are no nodes left to process
            if left > right:
                return None
                
            # 1. Grab the root from preorder using our pointer
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1
            
            # 2. Find the root's index in the inorder array instantly
            mid = inorder_map[root_val]
            
            # 3. Build the left and right subtrees
            # Left subtree gets everything strictly left of 'mid'
            root.left = build(left, mid - 1)
            
            # Right subtree gets everything strictly right of 'mid'
            root.right = build(mid + 1, right)
            
            return root
            
        # Start the recursive build using the full length of the inorder array
        return build(0, len(inorder) - 1)
