# Notes

## Idea
* BFS
* Traverse through the string
* Any time we find a prefix in which it exists in the dictionary, explore the rest of the string.
* If at any time we make it to the end, we know we were able to split the string into valid words
* Otherwise we return False

## Complexity
* Time complexity is *O(N^3)* since for each index, we can explore all substrings in the len(s)
* Space complexity is *O(N)*
