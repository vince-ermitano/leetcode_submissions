# Notes
* *Check out non-sorted version.*

## Idea
* Use same concept as TwoSumII where the array is sorted.
* For each element, run TwoSum on the elements to the right.
* For both loops in TwoSum and 3Sum, skip over an duplicate elements to avoid duplicates in the final answer.

## Complexity
* Time complexity is *O(N^2)* since we run TwoSum for every element in the nums array.
* Space complexity is dependent on sorting algorithm used. If ignoring that fact, it's *O(1)*
