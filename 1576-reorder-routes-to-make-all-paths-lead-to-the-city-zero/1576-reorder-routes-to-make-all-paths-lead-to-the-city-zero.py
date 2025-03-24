class Solution:
    # there are no cycles
    # create an adj list and track direction
    # start a dfs from node 0
    # when visiting a node, we know that a direction need to be flipped
    # by looking at the connection (adj list) between the node we are currently on
    # and the node that we came from
    # update the counter when a road needs to be flipped
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        counter = 0
        adj_list = defaultdict(list)
        visited = set()

        # create adjacency list
        for c in connections:
            adj_list[c[0]].append(c[1])
            adj_list[c[1]].append(-c[0])
        
        def dfs(curr):
            nonlocal counter, adj_list

            visited.add(curr)
        
            for neighbor in adj_list[curr]:
                if abs(neighbor) not in visited:
                    # check if we need to flip the road
                    if neighbor > 0:
                        counter += 1
                    
                    dfs(abs(neighbor))
            
        dfs(0)

        return counter 




