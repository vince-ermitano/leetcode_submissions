# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # keep two lengths as you traverse through the tree (dfs)
    # cannot go the same direction twice in a row
    # increase the length if going in the opposite direction
    # reset the length if going in the same direction
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        def dfs(root, left, right):
            if not root:
                return max(left, right)
            
            # traverse left
            l = dfs(root.left, right + 1, 0)
            # traverse right
            r = dfs(root.right, 0, left + 1)

            return max(l, r)
        
        return dfs(root, 0, 0) - 1

