class Solution:
    # Use graph traversal (bfs) to see if we can find a path for each query
    # Each variable will be a node in the graph
    # An edge from a node, A, to a node, B, denotes the equation A/B
    # The edge will have a value denoting the weight (i.e. the value of A/B)
    # If we have a node, X, and a node, Y, and want to find the answer for the query, X/Y,
    # we need to find a path from node X to node Y
    # The answer for the query will be the product of all the edge weights within the path from X -> Y.
    # If there is no path or if one of the nodes in the query does not exist in our graph, it is impossible to solve that query
    # To solve, run bfs for each query
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list) # node A -> [[B, A/B], ...]

        # populate adjacency list
        for i, eq in enumerate(equations):
            numerator, denominator = eq
            adj[numerator].append([denominator, values[i]]) # store equation given in equations
            adj[denominator].append([numerator, 1/values[i]]) # store inverse as well

        def bfs(src, target):
            # value not in equations
            if src not in adj or target not in adj:
                return -1

            q = deque()
            visited = set()
            q.append([src, 1])

            # run bfs
            while q:
                num, weight = q.popleft()
                visited.add(num)

                # found our denominator
                if num == target:
                    return weight
                # explore neighbors
                for nei in adj[num]:
                    if nei[0] not in visited:
                        q.append([nei[0], weight * nei[1]])
            
            # didn't find denominator
            return -1
                
        
        return [bfs(src, target) for src, target in queries]

