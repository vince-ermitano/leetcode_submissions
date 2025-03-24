# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # three cases
    # deleting a leaf node (trivial)
    # deleting a node with a single child -> make the child the new child of the parent node
    # deleting a node with both left and right children -> 
    #   * find inorder PREDECESSOR
    #   * replace value of successor with the node to be deleted
    #   * delete the predecessor
    # (can also do this with inorder successor)

    # get the inorder predecessor of a node
    def getPredecessor(self, root):
        curr = root.left

        while curr is not None and curr.right is not None:
            curr = curr.right
        
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return root


        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:

            
            if not root.left: # no children or only child is left
                return root.right
            if not root.right: # only child is right
                return root.left

            # has two children
            # swap root val with predecessor, then delete predecessor node
            predecessor = self.getPredecessor(root)
            root.val = predecessor.val
            root.left = self.deleteNode(root.left, predecessor.val)
        
        return root