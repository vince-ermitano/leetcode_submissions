"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def __init__(self):
                self.visited = {}
        
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        
        if node is None:
            return None
        
        if node in self.visited:
            return self.visited[node]
        
        new_node = Node(node.val, [])
        
        self.visited[node] = new_node
        
        if node.neighbors:
            new_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        
        return new_node
        
    