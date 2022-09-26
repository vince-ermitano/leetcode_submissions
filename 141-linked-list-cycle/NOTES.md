# Notes

## Idea
* Use a fast and slow pointer. 
* If the two ever meet then there is a cycle.
* If the fast pointer reaches the end of the linked list, then obviously there is no cycle.
* Can also just simply use HashSet to see if you visited a node already.

## Complexity
* Time complexity is *O(N)*. Imagine if the cyclic part of the linked list consisted of all the nodes. It will either take 1 or 2 extra passes of the fast pointer to catch up to the slow pointer depending on whether the number of nodes in the linked list is even or odd.
* Space complexity is *O(1)* since just keeping track of two pointers. Better compared to HashSet solution which is *O(N)*
