# Notes

## Idea
* Dynamic programming
* A cell, c_1's nearest distance to another cell c_2 with 0 is:
  * 0 if the c_1 contains 0
  * The minimum of its current distance, or the 1 + distance of it's neighboring cells' shortest distances to a 0.

## Complexity
* Time complexity is *O(r * c)* (two passes of the matrix)
* Space complexity is *O(1)* since the dp matrix is the output.
