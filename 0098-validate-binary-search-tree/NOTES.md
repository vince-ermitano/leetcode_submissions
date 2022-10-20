# Notes

## Idea
* Use recursion to test if the left and right subtrees are valid binary subtrees.
* Keep track of the boundaries in which a given node's value can be within as we recurse.

## Complexity
* Time complexity is *O(N)* to traverse through N nodes
* Space complexity is *O(N)* to the recursive stack called on *O(N)* nodes
