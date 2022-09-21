# Notes

## Idea/Approach
* Backtracking utilization obviously because this is exploring all possible combinations
* When traversing through list, simulate either taking the current number into the current combinations or not taking it.
* This will result in a tree-like structure that explores all possible combinations.
* We have checking in our backtracking algorithm to rule out any candidates that are not valid.

## Complexity
* Time complexity is the number of combinations to build which is *C(n, k)* and for each combination we need to build a combination of size *k* so *k * C(n, k)*
* Space complexity is determined by the storage of all the combinations so *O(C(n,k))*
