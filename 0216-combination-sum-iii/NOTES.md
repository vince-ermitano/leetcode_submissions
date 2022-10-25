# Notes

## Idea
* Backtracking
* Traverse through the digits 1-9 and calling the backtracking function where you add the current digit to the combination and one where you don't add the current digit to it. 
* This will allow the backtracking solution to explore able combinations, accepting the ones that are valid, and reject the ones that are not.

## Complexity
* Time complexity is *O(C(9, k))* to generate all combinations
* Space complexity is *O(K)* due to curr_combination holding k digits and recursive solution going k calls deep.
