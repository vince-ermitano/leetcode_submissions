# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # run dfs to traverse the tree
        # for each node you encounter run another dfs that sees if
        # starting at that node, we can find a path that adds up to the targetSum

        total = 0

        def dfs(root):
            if not root:
                return

            find_path(root, targetSum)
            dfs(root.left)
            dfs(root.right)
        
        def find_path(root, target):
            nonlocal total
            
            if not root:
                return
            
            if root.val == target:
                total += 1
            
            find_path(root.left, target - root.val)
            find_path(root.right, target - root.val)

        dfs(root)

        return total