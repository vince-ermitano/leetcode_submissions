# Notes

## Idea
* Use the characteristic of a BST to solve this problem
* If both p and q are greater than the subtree's root, then we know that both of them will be contained in the right subtree. Similar when they are both less.
* If they are not either of those cases, we know that they will have to be split up.

## Complexity
* Time complexity is *O(N)* where N is the # of nodes in the tree
* Space complexity is *O(N)* for the stack size due to the recursive calls on N nodes.
