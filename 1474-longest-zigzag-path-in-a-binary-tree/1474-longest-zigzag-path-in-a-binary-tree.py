# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # dfs to traverse consider each starting node
        # run another dfs to test length of zigzag path from that node
        # update res with max length

        longest = 0

        def dfs(root, left_length, right_length):
            nonlocal longest

            longest = max(longest, left_length, right_length)

            if root.left:
                dfs(root.left, 1 + right_length, 0)
            if root.right:
                dfs(root.right, 0, 1 + left_length)


        

        dfs(root, 0, 0)

        return longest