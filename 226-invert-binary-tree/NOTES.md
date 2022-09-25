# Notes

## Idea/Approach
* Use recursion to work on a small part of a tree at a time and build up to make the tree fully inverted
* Can do iteratively as well

## Complexity
* Time complexity is *O(N)* where *N* is the number of nodes because we just need to traverse through each node and swap its children
* Space complexity is *O(N)* where *N* is the number of nodes because of the stack frames due to the recursive behavior.
