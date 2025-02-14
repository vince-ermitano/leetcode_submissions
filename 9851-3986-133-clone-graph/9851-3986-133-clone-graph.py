"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        clones = {}

        def clone(node):
            if node in clones:
                return clones[node]
            
            new_node = Node(node.val)
            clones[node] = new_node
            new_node.neighbors = [clone(n) for n in node.neighbors]
            return new_node

        return clone(node) if node else None
        