# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
        
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        
        def recurse(node, level, ans):
            if node is None:
                return

            if len(ans) == level:
                ans.append([])

            ans[level].append(node.val)
            recurse(node.left, level + 1, ans)
            recurse(node.right, level + 1, ans)
        
        recurse(root, 0, ans)
        
        return ans
        
    
        