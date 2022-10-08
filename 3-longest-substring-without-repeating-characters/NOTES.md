# Notes

## Idea
* Use a hashmap to keep track of the current counts of each character in the current substring
* Any time the count of a character exceeds 1, keep removing from the left of the current substring until there are only unique characters.
* Update running max as we traverse through the string.

## Complexity
* Time complexity is *O(N)* since both (left and right) pointers can only go forwards.
* Space complexity is *O(N)* for the hashmap.
