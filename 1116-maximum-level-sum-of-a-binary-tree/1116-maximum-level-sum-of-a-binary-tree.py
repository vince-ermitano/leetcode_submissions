# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # bfs to find sum of each level
        # if sum of level is greater than largest sum we've seen
        # update our smallest level to that and update largest sum

        largest_sum = float('-inf')
        res = curr_level = 0
        q = deque()
        q.append(root)


        while q:
            curr_sum = 0
            curr_level += 1

            for i in range(len(q)):
                node = q.popleft()
                curr_sum += node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if curr_sum > largest_sum:
                largest_sum = curr_sum
                res = curr_level
        
        return res


