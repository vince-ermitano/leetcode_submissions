# Notes

## Idea
* Use two pointers, left and right, and initialize them to the start and end of the array respectively.
* Traverse array
* 3 cases
* If the sum of the elements at the two pointers equals target, return indices.
* If '                                          ' is less than target, move left pointer to the right once.
* If '                                          ' is greater than target, move right pointer to the left once.

## Complexity
* Time complexity is *O(N)*
* Space complexity is *O(1)*
