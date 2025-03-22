# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # maintain two lists containing the leaves for each tree
        # run dfs on each tree and add node to pertaining list if the node is a leaf

        def dfs(root, leaves):
            if not root:
                return
            
            if not root.left and not root.right:
                leaves.append(root.val)
            
            dfs(root.left, leaves)
            dfs(root.right, leaves)
        
        leaves_1 = []
        leaves_2 = []

        dfs(root1, leaves_1)
        dfs(root2, leaves_2)

        return leaves_1 == leaves_2
