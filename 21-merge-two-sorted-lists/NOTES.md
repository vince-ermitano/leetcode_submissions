# Notes

## Idea/Approach
* Maintain two pointers, one for each list.
* Create a new list
* Continue to add to the new list the smallest of the two numbers at each of the pointers.

## Complexity
* Time complexity is *O(N + M)* where N is # of nodes for list1 and M is the number of nodes for list2
* Space complexity is *O(1)* since we are only utilizing some pointers.

## Other
* Can solve recursively to minimize the code. This will affect the space complexity in terms of the stack frames, however.
