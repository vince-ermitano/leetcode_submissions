# Notes

## Idea
* DFS
* Make sure to consider edge case where the new color and the source of the flood fill are the same color or else solution might end up recursing forever.

## Complexity
* Time complexity is *O(n x m)* to search through the grid where n is the # of rows and m is the # of columns
* Space complexity is *O(n x m)* due to recursive behavior of the solution which performs DFS on the rows and columns of the grid.
