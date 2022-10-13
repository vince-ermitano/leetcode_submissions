# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if (root is None):
            return []
        
        q = deque()
        ans = []
        
        q.append(root)
        ans.append(root.val)
        
        while q:
            for i in range(len(q)):
                curr = q.popleft()

                if (curr.right is not None):
                    q.append(curr.right)
                if (curr.left is not None):
                    q.append(curr.left)
            
            if q:
                ans.append(q[0].val)
            
            
        return ans
            
        
        
        