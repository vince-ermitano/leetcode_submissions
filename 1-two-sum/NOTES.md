# Notes

## Idea/Approach
* Naive solution is to traverse through each number in array, and for each of those numbers, check each of all the other numbers to see if their sum equals the target.
* Quick solution is to take advantage of HashMap to quickly check if we've seen a number that we need already in the past
* For example, if *target = 8* and the current number we are looking at is 6, we want to quickly reference the HashMap to see if we've seen the number 2 already in the array

## Complexity
* Time complexity is *O(N)* to traverse through array
* Space complexity is *O(N)* to store the elements of the array in the HashMap
