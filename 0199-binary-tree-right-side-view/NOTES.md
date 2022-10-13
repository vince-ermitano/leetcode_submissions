# Notes

## Idea
* Use a queue to keep track of all the nodes on a current level.
* Make the first node that is added to the queue at each level the right most node.
* After traversing each level, append the node at the front of the queue to the answer

## Complexity
* Time complexity is *O(N)*
* Space complexity will be the diameter of the tree. This is just *O(N)*
