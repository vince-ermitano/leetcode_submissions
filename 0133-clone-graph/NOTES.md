# Notes

## Idea
* Use DFS/BFS to traverse through the graph and clone neighbors as you recurse.
* Use hashmap to avoid recursing infinitely on nodes that have already been visited

## Complexity
* Time complexity is *O(N + M)* where N is the # of nodes and M is the # of edges
* Space complexity is *O(N)* for the hashmap and the recursion stack
