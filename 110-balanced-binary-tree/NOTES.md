# Notes

## Idea
* Starting at the root node, recursively check 3 conditions:
  * If the height difference of its left and right subtree are <= 1
  * If the left subtree is itself balanced
  * If the right subtre is itself balanced
* If these 3 conditions are met, the tree is indeed balanced

## Complexity
* Time complexity is *O(NLOG(N))* where N is the # of nodes in the tree because for each node *p* at depth *d*, we will call height on p, d times.
* Space complexity is *O(N)* due to recursive stack calls
