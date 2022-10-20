# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def validate(self, root, lower, upper):
        if root == None:
            return True
        
        if root.val <= lower or root.val >= upper:
            return False
        
        return self.validate(root.left, lower, root.val) and self.validate(root.right, root.val, upper)
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.validate(root, -sys.maxint-1, sys.maxint)
        # return recurse(root.left, -sys.maxint-1, root.val) && recurse(root.right, root.val, sys.maxint)
    