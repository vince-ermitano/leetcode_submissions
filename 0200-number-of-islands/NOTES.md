# Notes

## Idea
* Traverse through grid
* Anytime we hit a '1', run dfs to explore that island, and increment the # of islands
* Make sure to keep track of which islands have been visited

## Complexity
* Time complexity is *O(n * m)* or the size of the grid
* Space complexity is *O(n * m)* in the case that the whole grid is an island and we need a recursion call for each cell
