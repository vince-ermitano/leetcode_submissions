# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:


        # return [x, y] 
        # where x = the max amount we can rob if we don't rob the curr house
        # where y = the max amount we can rob if we do rob the curr house
        def helper(root):

            if not root:
                return [0, 0] 

            left_max = helper(root.left)
            right_max = helper(root.right)

            # if we don't rob the curr house, we need to take the max of the values we could rob
            # from the prev houses (children) regardless of if we rob/don't rob them
            return [max(left_max) + max(right_max), root.val + left_max[0] + right_max[0]]

        return max(helper(root)[0], helper(root)[1])
        