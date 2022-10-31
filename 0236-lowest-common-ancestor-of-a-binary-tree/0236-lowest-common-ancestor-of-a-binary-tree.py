# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init_(self):
        self.ans = None
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        def recurse(root):
            if not root:
                return False
            
            mid = root == p or root == q
            
            left = recurse(root.left)
            right = recurse(root.right)
            
            if mid + left + right > 1:
                self.ans = root
            
            return mid or left or right
    
        
        recurse(root)
        return self.ans
    